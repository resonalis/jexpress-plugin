# Verification report — 2026-11-05

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
- [ ] Verify the exact OpenAI manifest schema and execute its validator. Schema URL and extension properties in the root manifests are **candidate values**, not certified compatible.
- [ ] Verify actual skill discovery and invocation in the target ChatGPT client, not merely file presence.
- [ ] Test two independent accounts for cross-session isolation, OAuth scopes, refresh after disconnect, and write confirmation.
- [x] **Refresh code-path review**: `worker/index.ts` refresh-token handler first calls `/inspect-refresh` then requires a successful live `AiSession /internal-summary` response before `/refresh` issues new tokens. Therefore a disconnected session cannot refresh through this exposed route while the live-session check rejects it. This is a source-level finding, not a disconnect/reconnect integration test.
- [ ] **Token cleanup**: `worker/oauthTokens.ts` `/revoke-session` still returns HTTP 503 (`live_session_validation_required`) rather than deleting token registrations. Live-session checks protect MCP and refresh routes, but implement explicit session token revocation before public release and test races/reconnection.
- [x] All five skill files were individually read from the feature branch; each contains YAML frontmatter with `name` and `description` and a domain-specific tool procedure. Actual ChatGPT skill discovery remains untested.
- [ ] Audit operational logs, telemetry, transient responses and exact retention against `PRIVACY.md`.
- [ ] Finalize Terms of Use and stable public URLs. `chatgpt/TERMS-DRAFT.md` is not an effective legal document.
- [ ] Review app permissions and reviewer onboarding in a separate browser/client before public submission.

## Release recommendation

**Do not submit yet.** Static source review found useful safeguards but cannot establish end-to-end authorization, revocation, isolation, privacy-retention or official manifest compliance.
