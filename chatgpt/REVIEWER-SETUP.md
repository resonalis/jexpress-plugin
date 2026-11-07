# Reviewer setup — J-Express for ChatGPT

**App:** J-Express (scientific research, non-clinical)
**MCP:** https://jexpress.resonalis.com/jexpress2026/mcp
**Workspace:** https://jexpress.resonalis.com/jexpress2026
**Demo:** Diauxic shift (bundled, synthetic/public research demo).
**Support:** https://github.com/resonalis/jexpress-plugin/issues
**Privacy / Terms:** https://resonalis.com/privacy/ · https://resonalis.com/terms/

The reviewer demo is **not an ordinary J-Express user account**. It is an isolated, password-protected entry point to the bundled scientific browser demo. The username/password must be provided **only** in the OpenAI review portal, not in the plugin package, source or public issues. There is no email verification, MFA or paid subscription.

## OpenAI portal: Reviewer credentials

- **Reviewer sign-in method:** Username and password
- **Login URL:** `https://jexpress.resonalis.com/jexpress2026/reviewer/login`
- **Tenant / workspace:** `J-Express Reviewer Demo`
- **Username:** `jexpress-reviewer`
- **Password:** Provisioned as the separate Cloudflare Worker secret `REVIEWER_DEMO_PASSWORD`; copy it from the owner's secure credential record. Never commit it to GitHub.
- **Access:** Read-only OAuth to the bundled educational gene-expression demo, with no access to other visitors' data.

## Reviewer workflow

1. Open the login URL above in the same browser profile used for the ChatGPT authorization window and enter the supplied credentials.
2. J-Express loads its bundled gene-expression example instead of any browser's previously saved project. The AI connection starts automatically. Keep this browser tab open; look for **Reviewer demo is ready** in AI connection.
3. Start J-Express OAuth connection from ChatGPT. An authorization URL opened in **the same browser profile** picks up the signed reviewer cookie and pairs only the demo's active browser session; it automatically approves only `dataset:read`. No request-ID copying or manual Approve click is required.
4. Run the supplied read-only scientific review cases. Use `list_datasets` first to obtain the actual dataset ID/name. The demo data and metadata are real bundled fixtures, not a fake tool response.
5. Disconnect the AI client or close the demo tab when finished. The browser session times out after roughly 30 minutes without renewal. The reviewer cookie lasts at most two hours, then sign-in is required again.

If a separate/incognito browser opens the OAuth page, its reviewer cookie will not be present and the normal manual pairing page appears. Return to the signed-in browser or log in there too.

## Operator deployment configuration

The production Cloudflare Worker `jexpress-web` must have **both** secret bindings before the reviewer login route becomes available: `REVIEWER_DEMO_PASSWORD` (random password at least 24 characters) and `REVIEWER_DEMO_SIGNING_KEY` (independent random signing secret at least 32 characters). Never put either into Wrangler config, the repository, the plugin ZIP or public review notes. The login is rate-limited per IP and the signed reviewer cookie is Secure, HttpOnly and SameSite=Lax. Only signed-in reviewer sessions can auto-approve demo OAuth; `dataset:read` is the maximum automatically granted scope.

## Review materials and caveats

- `plugin.json` automatically supplies five positive cases, three negative cases and initial release notes; use the secure submission portal for any additional reviewer-only instructions.
- Public explanatory video supplied by the project owner: https://youtu.be/uejBD_4fFkM . This is a broad product walkthrough. **A reviewer-specific screen recording that demonstrates the actual eight cases may still be required by OpenAI**; do not assume the overview video satisfies that requirement.
- No public user/account database is required. OAuth access is limited to the actively connected browser tab and approved scopes. A reviewer needs to complete the manual OAuth pairing in their own test browser; an inaccessible owner-only live session cannot serve as a reproducible fixture.
- The tool `read_dataset_slice` can disclose real numerical values and labels to the AI provider; use the bundled demo only.
- The source-preserving write tools are deliberately outside the five initial positive tests; they require separate consent and distinct OAuth scopes.
- Not clinically validated. Do not use identifiable patient data.
- If the submission portal reports failing automated checks, copy the findings back to the source project; the portable ZIP validation alone does not prove directory acceptance.
