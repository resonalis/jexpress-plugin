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

- [ ] **Live J-Express MCP tests blocked**: authorization/login was denied by the connected J-Express tool. Do not claim live success. Reconnect/approve and retry using non-sensitive demo data.
- [ ] Verify the exact OpenAI manifest schema and execute its validator. Schema URL and extension properties in the root manifests are **candidate values**, not certified compatible.
- [ ] Verify actual skill discovery and invocation in the target ChatGPT client, not merely file presence.
- [ ] Test two independent accounts for cross-session isolation, OAuth scopes, refresh after disconnect, and write confirmation.
- [ ] Review session/token invalidation: `worker/oauthTokens.ts` `/revoke-session` returns HTTP 503 (`live_session_validation_required`); protected MCP requests check live session, but the token registry itself does not revoke on that endpoint. Confirm refresh cannot reactivate a disconnected browser session.
- [ ] Audit operational logs, telemetry, transient responses and exact retention against `PRIVACY.md`.
- [ ] Finalize Terms of Use and stable public URLs. `chatgpt/TERMS-DRAFT.md` is not an effective legal document.
- [ ] Review app permissions and reviewer onboarding in a separate browser/client before public submission.

## Release recommendation

**Do not submit yet.** Static source review found useful safeguards but cannot establish end-to-end authorization, revocation, isolation, privacy-retention or official manifest compliance.
