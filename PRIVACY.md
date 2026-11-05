# J-Express AI plugin privacy policy

Last updated: 5 November 2026

This policy describes the J-Express AI integration for supported clients, including Claude and ChatGPT, using the MCP server at `https://jexpress.resonalis.com/jexpress2026/mcp`.

## Browser workspace and data flows

J-Express runs in your browser. Your loaded datasets, annotations, selections and analyses are processed in the J-Express workspace. The plugin package provides connection information and scientific workflow guidance; it does not install local executable software.

When you authorize an AI client and it invokes a J-Express MCP tool, the request passes through the J-Express server to your connected browser session. The result returns through that server to the requesting AI client. Depending on the tool and permissions granted, results **may include raw numeric matrix values, dataset identifiers, row/column names, sample annotations, quality metrics, analysis results and exported plot images**. Such information is disclosed to the AI provider when returned to its client.

## Connection records and temporary processing

The J-Express server uses connection/session state, OAuth client registration and token records to authenticate and route requests. Access tokens have a nominal 15-minute lifetime; refresh tokens may remain valid for up to 30 days, subject to session authorization. Token hashes, rather than raw token values, are stored in the token registry.

The server may temporarily hold requests and tool responses while delivering them to the browser or AI client. Session records and transient request/result state are maintained by the service infrastructure. These are not equivalent to storing a permanent copy of your full dataset. Exact retention and deletion behavior, as well as operational logging and optional telemetry, are subject to a separate implementation audit before public release.

## Your controls

You choose whether to connect an AI client, review its requested permissions, and may disconnect the workspace. Permissions may include reading data, creating derived analyses or datasets, modifying data through authorized tools, and capturing plots. Datasets are locked against matrix edits by default; supported edit operations are designed to preserve source data by creating derived datasets. Review each requested action and permission carefully.

## AI providers and third parties

Information sent to ChatGPT is governed by OpenAI's applicable terms and privacy practices; information sent to Claude is governed by Anthropic's applicable terms and privacy practices. Resonalis does not control how these independent providers handle information you choose to share with them.

J-Express infrastructure is hosted using Cloudflare services. The plugin does not intentionally sell dataset content or use it for advertising. No guarantee is made here about a third-party AI provider's model-training practices.

## Contact

Resonalis — contact@resonalis.com.

**Publication note:** This document must be reviewed against the deployed server's actual logging, retention, telemetry and deletion behavior before it is represented as the final public privacy notice.
