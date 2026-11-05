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

## Private installation smoke test

A private J-Express 0.1.0 test plugin was imported successfully from the GitHub Actions ZIP into a personal ChatGPT account. To finish runtime verification, install/activate that private plugin from the ChatGPT Plugins page (the private link is supplied to the owner directly), then start **a new conversation**. Check that all five skills are discoverable and that a read-only query on the demo `diauxic shift` calls the **new private plugin** MCP connection, not a pre-existing development connector. Ask for a matrix-analysis workflow; verify other skills with a separate request for their respective workflow guidance, without performing writes. Log exact client/plugin identity and tool calls.

The private import automatically normalized developer identity to the importing personal account; public submission must select and verify the intended Resonalis publisher.

## Publication checklist
- [x] Validate portable `plugin.json` and `mcp.json` against Agent Plugins 1.0.0 official JSON schemas in [GitHub Actions](https://github.com/resonalis/jexpress-plugin/actions/runs/42101736196), and import the ZIP successfully with OpenAI's private Plugin Creator. The public submission portal scan remains pending.
- [x] Confirm all five original skills were included in the imported private plugin, with exact content matches against the source repo.
- [ ] Activate the private plugin in a fresh ChatGPT conversation and prove all five skills are discoverable and invokable at runtime. Private package import is not proof of activation.
- [ ] Test OAuth with an independent account and verify cross-user session isolation, scopes, token revocation, and write consent.
- [ ] Audit deployed storage, logging, telemetry and retention against the updated platform-neutral privacy policy; remove the publication note only after review. Publish final Terms of Use at a stable public URL.
- [ ] Verify logo sizing, screenshot requirements, support and reviewer access.
- [ ] Obtain explicit approval before submission.

Do not reuse the Claude-specific `.claude-plugin/plugin.json` as a ChatGPT manifest. Do not modify the production MCP URL for packaging alone.
