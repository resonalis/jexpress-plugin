# J-Express for ChatGPT — publishing package

Status: **preparation only**. This repository is not evidence that J-Express is approved or listed in the ChatGPT app/plugin directory.

## Shared integration
- MCP endpoint: `https://jexpress.resonalis.com/jexpress2026/mcp`
- Application: `https://jexpress.resonalis.com/jexpress2026`
- Publisher: Resonalis
- Contact: `contact@resonalis.com`
- Scientific guidance: the five shared `../skills/jexpress-*/SKILL.md` files.
- Product icon: [`../assets/jexpress-logo.svg`](../assets/jexpress-logo.svg), copied from the J-Express application's canonical `public/jexpress-logo.svg` (square 512×512 SVG wrapper).
- Publisher mark: [`../assets/resonalis-logo.svg`](../assets/resonalis-logo.svg), copied from the approved Resonalis emblem used on the Resonalis website. This is a separate publisher branding asset, **not** the J-Express application icon.
- The legacy Claude image [`../.claude-plugin/icon.png`](../.claude-plugin/icon.png) remains unchanged.
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

**Publisher identity limitation:** OpenAI's private personal-plugin import normalizes the displayed publisher/developer name to the importing personal account. Both root `author` and OpenAI `interface.developerName` in this repository are `Resonalis`, but this alone cannot remove the personal name shown on a `USER`-scoped private plugin. To publish with `Av Resonalis`, select/create a **verified Resonalis developer identity/workspace** in the publication workflow. Do not misrepresent the personal private plugin as company-published.

**Icon rendering:** The old Claude PNG already contained the correct J-Express glyph, but the personal plugin card displayed a default star. The portable manifest now points to the official product SVG under `assets/`. This fixes asset mapping; actual rendering is controlled by the ChatGPT client/catalog and must be checked after refreshing/installing the new private release. The Resonalis SVG is included for future publisher branding but **cannot be forced as a separate publisher avatar using the portable interface fields**.

## Publication checklist
- [x] Validate portable `plugin.json` and `mcp.json` against Agent Plugins 1.0.0 official JSON schemas in [GitHub Actions](https://github.com/resonalis/jexpress-plugin/actions/runs/42101736196), and import the ZIP successfully with OpenAI's private Plugin Creator. The public submission portal scan remains pending.
- [x] Confirm all five original skills were included in the imported private plugin, with exact content matches against the source repo.
- [ ] Activate the private plugin in a fresh ChatGPT conversation and prove all five skills are discoverable and invokable at runtime. Private package import is not proof of activation.
- [ ] Test OAuth with an independent account and verify cross-user session isolation, scopes, token revocation, and write consent.
- [ ] Audit deployed storage, logging, telemetry and retention against the updated platform-neutral privacy policy; remove the publication note only after review. Publish final Terms of Use at a stable public URL.
- [x] Package and validate square J-Express and Resonalis SVG brand assets, with `composerIcon` and `logo` both pointing to the J-Express product mark.
- [ ] Verify rendering of the J-Express icon in the ChatGPT UI and separately configure the verified Resonalis publisher identity; manifest fields alone do not control the personal account byline.
- [ ] Verify screenshot requirements, support and reviewer access.
- [ ] Obtain explicit approval before submission.

Do not reuse the Claude-specific `.claude-plugin/plugin.json` as a ChatGPT manifest. Do not modify the production MCP URL for packaging alone.
