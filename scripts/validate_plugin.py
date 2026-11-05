#!/usr/bin/env python3
"""Validate a portable J-Express plugin against Agent Plugins 1.0.0 schemas.

Usage: python scripts/validate_plugin.py [root]
Requires: python -m pip install jsonschema PyYAML
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.request import urlopen

from jsonschema import Draft202012Validator
import yaml

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
schema_root = "https://agent-plugins.org/schemas/1.0.0/"
expected = {
    "plugin.json": "plugin.schema.json",
    "mcp.json": "mcp.schema.json",
}

for filename, schema_filename in expected.items():
    target = root / filename
    data = json.loads(target.read_text(encoding="utf-8"))
    schema_url = schema_root + schema_filename
    with urlopen(schema_url, timeout=15) as response:
        schema = json.load(response)
    errors = sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: str(e.path))
    if errors:
        for error in errors:
            print(f"FAIL {filename}: {'.'.join(map(str, error.path))}: {error.message}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS {filename}: {schema_url}")

manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
mcp = json.loads((root / "mcp.json").read_text(encoding="utf-8"))
assert manifest["name"] == "jexpress"
assert manifest["version"]
assert len(mcp["mcpServers"]) == 1
assert mcp["mcpServers"]["jexpress"]["type"] == "streamable-http"
assert mcp["mcpServers"]["jexpress"]["url"] == "https://jexpress.resonalis.com/jexpress2026/mcp"

openai = manifest.get("extensions", {}).get("com.openai", {})
interface = openai.get("interface", {})
for field in ("composerIcon", "logo"):
    path = interface.get(field)
    if path:
        assert path.startswith("./") and ".." not in Path(path).parts, (field, path)
        assert (root / path).is_file(), f"Missing {field}: {path}"
for field in ("websiteURL", "privacyPolicyURL", "supportURL"):
    assert interface[field].startswith("https://"), f"Invalid {field}"
print("PASS OpenAI manifest references and endpoints")

expected_skills = {
    "jexpress-matrix-analysis",
    "jexpress-normalization",
    "jexpress-bulk-rnaseq",
    "jexpress-single-cell-rnaseq",
    "jexpress-embeddings",
}
actual = set()
for path in sorted((root / "skills").glob("*/SKILL.md")):
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"Missing skill YAML header: {path}"
    header = text.split("---", 2)[1]
    metadata = yaml.safe_load(header)
    assert isinstance(metadata, dict)
    assert metadata.get("name") == path.parent.name, f"Wrong skill name: {path}"
    assert isinstance(metadata.get("description"), str) and metadata["description"].strip(), f"Empty description: {path}"
    assert len(text.split("---", 2)[2].strip()) > 200, f"Skill has insufficient instructions: {path}"
    actual.add(path.parent.name)
assert actual == expected_skills, f"Skills mismatch: {expected_skills ^ actual}"
print(f"PASS {len(actual)} SKILL.md frontmatter and bodies: {', '.join(sorted(actual))}")
print("PASS portable plugin preflight (the OpenAI submission portal may impose additional requirements)")
