# J-Express AI plugin privacy policy

Last updated: 7 November 2026

This policy describes the J-Express AI integration for supported clients, including Claude and ChatGPT, using the MCP server at `https://jexpress.resonalis.com/jexpress2026/mcp`.

## Browser workspace and data flows

J-Express runs in your browser. Your loaded datasets, annotations, selections and analyses are processed in the J-Express workspace. The plugin package provides connection information and scientific workflow guidance; it does not install local executable software.

When you authorize an AI client and it invokes a J-Express MCP tool, the request passes through the J-Express server to your connected browser session. The result returns through that server to the requesting AI client. Depending on the tool and permissions granted, results **may include raw numeric matrix values, dataset identifiers, row/column names, sample annotations, quality metrics, analysis results and exported plot images**. Such information is disclosed to the AI provider when returned to its client.

## Connection records and temporary processing

The J-Express server uses Cloudflare Durable Objects for connection/session state, OAuth client registration and token records. A browser connection sends an allowlisted technical context (dataset type/size and selected numeric analysis metadata) to the relay before any AI client is approved; matrix values and identifiers are not included in this initial context. A connected browser renews its session, which otherwise expires after about 30 minutes. Access tokens expire after 15 minutes; refresh tokens have a maximum 30-day validity. The OAuth registry stores hashes of tokens, not the bearer or refresh-token strings. Dynamic client registrations expire after 30 days of inactivity; pending requests expire in 5 minutes and authorization codes in about 1 minute.

The relay may temporarily store a queued MCP request and its response, including the returned scientific data, while passing it between your browser and the approved AI client. Results are deleted when collected and otherwise become eligible for cleanup after about 60 seconds. Expiration is checked when records are used, while actual deletion can be delayed by periodic cleanup, provider retention or backups. This is not a permanent server-side dataset repository.

**Disconnect and revoke:** the live relay denies MCP access as soon as browser sharing is inactive. The production Worker deployed on 7 November 2026 is designed to delete associated access/refresh records on an authenticated Disconnect/Revoke, purge queued requests and results, and keep a session-ID-only revocation marker for up to 31 days to prevent credential reactivation. Source-level tests and deployment succeeded. Independent-client integration testing and verification of Cloudflare provider-side storage and deletion remain outstanding; data already received by an AI provider cannot be withdrawn.

For OAuth dynamic client-registration abuse prevention, J-Express temporarily stores a rate-limit key derived from the caller's IP address (IPv6 grouped to a /64 prefix), with approximately one-hour expiry. This technical network information is separate from optional anonymous usage counts.

## Your controls

You choose whether to connect an AI client, review its requested permissions, and may disconnect the workspace. Permissions may include reading data, creating derived analyses or datasets, modifying data through authorized tools, and capturing plots. Datasets are locked against matrix edits by default; supported edit operations are designed to preserve source data by creating derived datasets. Review each requested action and permission carefully.

## AI providers and third parties

Information sent to ChatGPT is governed by OpenAI's applicable terms and privacy practices; information sent to Claude is governed by Anthropic's applicable terms and privacy practices. Resonalis does not control how these independent providers handle information you choose to share with them.

J-Express infrastructure is hosted using Cloudflare services. Optional J-Express usage statistics (enabled by default, disable in the app or with `?telemetry=off`) send only allowlisted event/analysis categories and a count to Cloudflare Analytics Engine; they contain no matrix values, names or persistent user IDs. This does **not** mean the host is unable to see IP addresses, timestamps or request metadata.

A read-only inspection of the production Worker on 6 November 2026 found `logpush: false` and no Tail Worker consumers. This does not establish that Cloudflare account-wide security/diagnostic logs, analytics retention or backups are absent; their exact retention has not been independently verified. The plugin does not intentionally sell dataset content or use it for advertising. No guarantee is made here about a third-party AI provider's model-training practices.

## Contact

Resonalis — contact@resonalis.com.

This notice describes documented application behavior and selected live infrastructure settings, not external security, privacy or clinical certification. We cannot guarantee deletion of third-party provider logs or copies already received by a connected AI client.
