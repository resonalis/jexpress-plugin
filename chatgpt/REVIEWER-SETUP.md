# Reviewer setup — J-Express for ChatGPT

**App:** J-Express (scientific research, non-clinical)
**MCP:** https://jexpress.resonalis.com/jexpress2026/mcp
**Workspace:** https://jexpress.resonalis.com/jexpress2026
**Demo:** Diauxic shift (bundled, synthetic/public research demo).
**Support:** https://github.com/resonalis/jexpress-plugin/issues
**Privacy / Terms:** https://resonalis.com/privacy/ · https://resonalis.com/terms/

No J-Express user account, password, email code, MFA, or confidential dataset is needed. A local browser tab is needed because J-Express runs the analysis on the connected browser client. The reviewer must approve one OAuth pairing request in that tab. Do not put tokens or session secrets into the reviewer-information form.

## Prepare the public demo

1. In one browser tab, open J-Express and load the bundled **Diauxic shift** dataset. Leave the tab open and the demo selected.
2. Expand **AI connection**, choose **Connect**, then keep this J-Express tab open.
3. In the ChatGPT plugin submission portal choose **With MCP**, connect the production HTTPS endpoint, and complete the displayed domain challenge (the challenge token comes from the portal and cannot be pre-filled).
4. On OAuth authorization, copy the UUID request ID from the authorization page into the J-Express **OAuth request ID** input. Check the actual client and return host, review scopes, approve **dataset:read**; optional project write and view capture scopes are not necessary for the five positive review cases.
5. Return to the ChatGPT connection and complete authorization. Use the positive and negative prompts imported from `plugin.json`. Dataset ID may vary: resolve it from `list_datasets` rather than hardcoding one.
6. After testing, click **Disconnect** in the J-Express browser tab. No AI tool can read the data after disconnect.

## Review materials and caveats

- `plugin.json` automatically supplies five positive cases, three negative cases and initial release notes; use the secure submission portal for any additional reviewer-only instructions.
- Public explanatory video supplied by the project owner: https://youtu.be/uejBD_4fFkM . This is a broad product walkthrough. **A reviewer-specific screen recording that demonstrates the actual eight cases may still be required by OpenAI**; do not assume the overview video satisfies that requirement.
- No public user/account database is required. OAuth access is limited to the actively connected browser tab and approved scopes. A reviewer needs to complete the manual OAuth pairing in their own test browser; an inaccessible owner-only live session cannot serve as a reproducible fixture.
- The tool `read_dataset_slice` can disclose real numerical values and labels to the AI provider; use the bundled demo only.
- The source-preserving write tools are deliberately outside the five initial positive tests; they require separate consent and distinct OAuth scopes.
- Not clinically validated. Do not use identifiable patient data.
- If the submission portal reports failing automated checks, copy the findings back to the source project; the portable ZIP validation alone does not prove directory acceptance.
