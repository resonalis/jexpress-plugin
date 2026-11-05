# J-Express for ChatGPT — publishing package

Status: **preparation only**. This repository is not evidence that J-Express is approved or listed in the ChatGPT app/plugin directory.

## Shared integration
- MCP endpoint: `https://jexpress.resonalis.com/jexpress2026/mcp`
- Application: `https://jexpress.resonalis.com/jexpress2026`
- Publisher: Resonalis
- Contact: `contact@resonalis.com`
- Scientific guidance: the five shared `../skills/jexpress-*/SKILL.md` files.
- Artwork: `../.claude-plugin/icon.png` (confirm required dimensions and rights for the target directory).
- Privacy policy: `../PRIVACY.md` (now cross-platform; retention and telemetry claims still require production verification).

## Proposed listing copy
**Name:** J-Express

**Short description:** Explore scientific datasets, run reproducible analyses, inspect plots, and create derived datasets through a connected J-Express workspace.

**Description:** Connect ChatGPT to a J-Express browser session to explore numeric matrices, embeddings, bulk RNA-seq and single-cell RNA-seq data. Inspect metadata and quality metrics, plan and run supported analyses, and review visualizations. The five scientific skills provide domain-specific analysis procedures and limitations. Results require scientific interpretation; this is not a validated clinical diagnostic tool.

## Reviewer onboarding
1. Open the J-Express application in a browser tab and load a non-sensitive demo dataset.
2. Start **AI connection** and keep the browser tab open.
3. Add/connect the MCP endpoint in ChatGPT using the supported authentication flow.
4. Review the OAuth client, redirect host, and requested scopes in J-Express; approve only intended access.
5. Try `list_datasets`, `read_dataset_details`, and a read-only quality/analysis capability query.
6. Disconnect in J-Express and verify further requests fail.

## Publication checklist
- [ ] Validate the root `plugin.json` and `mcp.json` against the current OpenAI packaging specification and run the actual submission validator. These files are candidates, not proof of compatibility.
- [ ] Verify that the five shared skills are discovered and invoked in the target ChatGPT client; repository presence alone does not establish runtime availability.
- [ ] Test OAuth with an independent account and verify cross-user session isolation, scopes, token revocation, and write consent.
- [ ] Audit deployed storage, logging, telemetry and retention against the updated platform-neutral privacy policy; remove the publication note only after review. Publish final Terms of Use at a stable public URL.
- [ ] Verify logo sizing, screenshot requirements, support and reviewer access.
- [ ] Obtain explicit approval before submission.

Do not reuse the Claude-specific `.claude-plugin/plugin.json` as a ChatGPT manifest. Do not modify the production MCP URL for packaging alone.
