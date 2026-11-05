# J-Express for ChatGPT — publishing package

Status: **preparation only**. This repository is not evidence that J-Express is approved or listed in the ChatGPT app/plugin directory.

## Shared integration
- MCP endpoint: `https://jexpress.resonalis.com/jexpress2026/mcp`
- Application: `https://jexpress.resonalis.com/jexpress2026`
- Publisher: Resonalis
- Contact: `contact@resonalis.com`
- Scientific guidance: the five shared `../skills/jexpress-*/SKILL.md` files.
- Artwork: `../.claude-plugin/icon.png` (confirm required dimensions and rights for the target directory).
- Existing privacy policy: `../PRIVACY.md` (currently Claude-specific; must be reviewed and updated before ChatGPT publication).

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
- [ ] Confirm current OpenAI submission and packaging specification from official documentation; create a platform-specific manifest only after its schema is verified.
- [ ] Decide whether skills are packaged with the plugin or exposed through another supported mechanism, and verify their discovery in the target ChatGPT client.
- [ ] Test OAuth with an independent account and verify cross-user session isolation, scopes, token revocation, and write consent.
- [ ] Publish an accurate **platform-neutral** privacy policy and public Terms of Use; confirm storage/retention claims against server implementation.
- [ ] Verify logo sizing, screenshot requirements, support and reviewer access.
- [ ] Obtain explicit approval before submission.

Do not reuse the Claude-specific `.claude-plugin/plugin.json` as a ChatGPT manifest. Do not modify the production MCP URL for packaging alone.
