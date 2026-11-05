# J-Express plugin privacy policy

Last updated: 5 November 2026

This policy covers the J-Express plugin for Claude and the J-Express MCP server at `https://jexpress.resonalis.com/jexpress2026/mcp` that the plugin connects to.

## Where your data is

J-Express runs in your web browser. Your datasets, metadata, selections and saved analyses stay in that browser. The plugin itself contains only instructions (skills) and the address of the MCP server; it runs no code on your computer.

## What passes through the server

When Claude calls a J-Express tool, the request goes to the J-Express server, which hands it to the J-Express tab you have open and authorized. The tab computes the answer, and the server passes it back to Claude. Depending on the tool, an answer can contain dataset names and dimensions, summary and quality statistics, bounded slices of matrix values, row or column labels, analysis results, or an image of a J-Express view.

The server holds a request or an answer only while it is being delivered. An answer is deleted as soon as Claude has received it, and one that is never collected is deleted after about one minute.

## What the server stores

- **Connection session.** A pairing between your browser tab and Claude, with a summary of the active dataset's type and size. It expires 30 minutes after the last activity, or when you disconnect.
- **OAuth records.** Access tokens (valid for 15 minutes), refresh tokens (30 days) and the registration of the Claude client (removed after 30 days without use). Tokens are stored as hashes.

The server does not sell, share or use your data for advertising or for training models. Data that reaches Claude is handled under Anthropic's own terms and privacy policy.

## Your choices

You decide whether to connect, and you approve each connection in J-Express. You can disconnect at any time, and J-Express works without any AI connection. Datasets are locked against changes by default; tools that change data create new child datasets and need your explicit unlock and confirmation.

## Contact

J-Express and this plugin are provided by Resonalis. Questions about this policy: contact@resonalis.com.
