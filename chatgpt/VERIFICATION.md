# Verification report — updated 2026-11-06

Scope: static review of `resonalis/jexpress-plugin` and current `bdysvik/jexpress` worker source. **Not** a completed external ChatGPT submission or end-to-end OAuth test.

## Completed checks

- [x] Repository contains five skill folders with `SKILL.md`.
- [x] Claude plugin manifest and `.mcp.json` still exist, independent of the new root `plugin.json` and `mcp.json`.
- [x] Both platform configurations refer to the same HTTPS MCP URL: `https://jexpress.resonalis.com/jexpress2026/mcp`.
- [x] Root `plugin.json` and `mcp.json` were reviewed as JSON source (not yet validated by an official ChatGPT plugin packager).
- [x] Privacy notice updated to describe both ChatGPT and Claude and explicitly warn that raw values, annotations and plots may be disclosed to the connected AI provider.
- [x] Worker source `worker/index.ts` checks bearer token validation and a live AI session before protected MCP calls.
- [x] Token registry `worker/oauthTokens.ts` specifies 15-minute access tokens and 30-day refresh tokens; refresh rotates credentials.
- [x] `src/core/mcpToolScopes.ts` maps read, project-write and dataset-modify scopes; unknown tools do not automatically receive read access.

## Blockers / required live verification

- [x] **Bounded raw-data read via J-ExpressDeploy**: `read_dataset_slice` returned exactly 2 rows × 3 columns from `diauxic shift`, including row labels, column metadata and six numeric matrix values. This verifies that the authorized connector can disclose raw data as described in the privacy policy.
- [x] **Read-only live MCP smoke test via J-ExpressDeploy**: `list_datasets`, `list_scientific_capabilities`, `read_dataset_details`, `inspect_dataset_quality`, and `propose_analysis_workflow` succeeded against `diauxic shift` (391 rows × 7 columns). Quality scan completed 2,737 values and found 4 missing values; the workflow correctly required review and did not execute analysis. This verifies the currently authorized Deploy connection, **not** new-plugin installation or cross-account OAuth.
- [ ] `get_dataset_lock` was blocked by OpenAI's security control; no lock-state conclusion can be drawn. Earlier direct J-Express connector calls were denied; use Deploy for subsequent live checks.
- [x] Portable manifests passed canonical Agent Plugins 1.0.0 JSON Schema checks in GitHub Actions and private package import. Submission portal validation is pending.
- [x] All five skills were packaged and imported byte-for-byte. **Runtime activation and invocation in a fresh ChatGPT client session remain pending.**
- [ ] Test two independent accounts for cross-session isolation, OAuth scopes, refresh after disconnect, and write confirmation.
- [x] **Refresh code-path review**: `worker/index.ts` refresh-token handler first calls `/inspect-refresh` then requires a successful live `AiSession /internal-summary` response before `/refresh` issues new tokens. Therefore a disconnected session cannot refresh through this exposed route while the live-session check rejects it. This is a source-level finding, not a disconnect/reconnect integration test.
- [x] **Token cleanup implemented on an unmerged feature branch:** [J-Express PR #66](https://github.com/bdysvik/jexpress/pull/66) implements `/revoke-session` token deletion + 31-day deny markers, owner-authorized disconnect/revoke, and in-flight result blocking; [targeted CI passed](https://github.com/bdysvik/jexpress/actions/runs/42221134666). This is **not deployed yet**.
- [ ] **Live post-deploy**: verify two independent client/account OAuth flows, revoked refresh tokens, reconnect and in-flight read cancellation on the actual production worker.
- [x] All five skill files were individually read from the feature branch; each contains YAML frontmatter with `name` and `description` and a domain-specific tool procedure. Actual ChatGPT skill discovery remains untested.
- [x] **Implementation/Worker configuration audit**: [2026-11-06 technical report](https://github.com/bdysvik/jexpress/blob/feature/chatgpt-oauth-revocation/docs/validation/chatgpt-oauth-privacy-audit-2026-11-06.md) covers Cloudflare Durable Object retention, authentication records, ephemeral MCP results, IP-address rate limiting and analytics. Live Worker `jexpress-web` reports `logpush: false`, no Tail Worker consumers, and `observability: null`.
- [ ] **Provider/production verification still required**: confirm account-wide Cloudflare security/log retention, backend expiry/cleanup after deployment and independent AI-provider retention. Source/Worker settings alone cannot establish the absence of all logs.
- [ ] Finalize Terms of Use and stable public URLs. `chatgpt/TERMS-DRAFT.md` is not an effective legal document.
- [ ] Review app permissions and reviewer onboarding in a separate browser/client before public submission.

## Plugin packaging and private import — 2026-11-05

- [x] Canonical Agent Plugins 1.0.0 JSON Schemas validated in GitHub Actions; `mcp.json` now uses the strict portable Streamable HTTP variant.
- [x] GitHub Actions run [42101736196](https://github.com/resonalis/jexpress-plugin/actions/runs/42101736196) **succeeded** and built `jexpress-chatgpt-plugin.zip` from the exact repository source files.
- [x] Imported the ZIP successfully with OpenAI Plugin Creator as **jexpress** 0.1.0 (personal, PRIVATE; ID `plugins_6aece47f9fe88191839b169360adc341`).
- [x] Inspected private package: original portable manifests, generated compatibility files and all five scientific skills are present. Compared imported skill files against GitHub originals: **all five exact matches**.
- [ ] **Client runtime**: installing/activating [the private plugin](https://chatgpt.com/plugins/plugins_6aece47f9fe88191839b169360adc341) and invoking each skill in a fresh ChatGPT conversation remains. Skills from an existing development J-Express plugin are not evidence this private plugin is active.
- [ ] **Public submission**: With MCP tool scan/review and policy checks in OpenAI's submission portal remain.
- [x] **Publisher plan:** use the current personal developer identity for initial release (the owner accepted the personal byline); consider a future Resonalis AS publisher identity later, subject to platform migration rules.
- [ ] **Privacy link**: plugin manifest links `main/PRIVACY.md`, but cross-platform privacy revisions are branch-only until merged.

## Branding verification — 2026-11-05

- [x] Imported the canonical J-Express 7-hexagon SVG from `bdysvik/jexpress/public/jexpress-logo.svg` into `assets/jexpress-logo.svg`, adjusted only for square image sizing. It is referenced by **both** portable OpenAI `interface.logo` and `interface.composerIcon`.
- [x] Added the **exact** Resonalis website branding file `bdysvik/molmine-website/public/assets/Rlogo.webp` as `assets/resonalis-logo.webp` and removed the incorrect alternate SVG. The WebP is separate from the J-Express application icon.
- [x] Portable manifest author: `Resonalis <contact@resonalis.com>`. OpenAI interface: `developerName: Resonalis`.
- [x] GitHub Actions run [42106063691](https://github.com/resonalis/jexpress-plugin/actions/runs/42106063691) passed square-image and manifest checks, packaged both assets, and uploaded a test ZIP.
- [x] Updated existing personal private plugin through **v0.1.2**. Readback verifies `author.name: Resonalis`, `developerName: Resonalis`, J-Express SVG app icon and the actual Resonalis WebP publisher asset. The personal ChatGPT card may still show the owner-account byline.
- [ ] **Observed ChatGPT UI byline/icon still need owner verification.** Personal scope remains `USER`; even with `developerName: Resonalis` in normalized metadata, OpenAI may display the private importing account's verified identity. The old card showed a default star despite the old PNG already containing the J-Express logo; new SVG mapping is accepted but on-screen rendering cannot be checked by tool.
- [ ] If/when Resonalis AS is founded and independently verified, assess whether OpenAI supports moving the listing to the company developer identity. The portable manifest does not control the account-level byline.

## Release recommendation

**Do not submit yet.** The new revocation implementation passes focused tests but is not deployed. Live two-client isolation/reconnect checks, provider retention confirmation and public submission portal checks remain.
