# J-Express for Claude

J-Express is a browser-based application for exploring and analyzing numeric matrices: gene expression, bulk and single-cell RNA-seq, proteomics and text embeddings. This plugin connects Claude to your J-Express session and adds five analysis skills that tell Claude how to plan and run careful, reproducible analyses with the J-Express tools.

**Status: preview (0.1.0).** The skills are still being validated against the J-Express tools. They have not been scientifically validated, and their results should be reviewed by someone qualified to judge them.

## What's included

**MCP server.** The plugin adds the J-Express MCP server at `https://jexpress.resonalis.com/jexpress2026/mcp`. Its tools list and inspect datasets, check data quality, propose analysis workflows, run analyses (PCA, K-means, hierarchical clustering, correspondence analysis, UMAP, neighbor graphs, Leiden clustering, embedding search), create filtered or normalized child datasets, and show J-Express views.

**Skills.**

| Skill | Use it for |
| :- | :- |
| `jexpress-matrix-analysis` | PCA, correspondence analysis, clustering, heatmaps, profiles and descriptive group comparisons on general numeric matrices |
| `jexpress-normalization` | Choosing and applying a normalization, transformation or scaling that fits the data type |
| `jexpress-bulk-rnaseq` | Design-aware QC, filtering, normalization and exploratory analysis of bulk RNA-seq count matrices |
| `jexpress-single-cell-rnaseq` | Single-cell QC, highly variable genes, PCA, neighbor graphs, Leiden clusters and UMAP |
| `jexpress-embeddings` | Nearest neighbors, semantic search, PCA/UMAP and concept directions on embedding vectors |

Each skill states what J-Express can and cannot do today. For example, inferential differential expression with a count-based model is not available yet, and the skills tell Claude to report that rather than substitute a weaker test.

## Requirements

- A J-Express session open in your browser at https://jexpress.resonalis.com/jexpress2026.
- Sign-in to the MCP server. The first time Claude uses it, you are asked to authorize the connection to your J-Express session (OAuth).

## Install

- **claude.ai, Claude Desktop and Cowork:** add **J-Express** from the plugin directory under **Customize → Plugins**, then connect the J-Express connector on the plugin's **Connectors** tab.
- **Claude Code:** run `claude plugin marketplace add resonalis/jexpress-plugin`, then `claude plugin install jexpress@jexpress`.

## Data and privacy

Your datasets stay in your browser. When Claude calls a J-Express tool, the request goes to the J-Express server at `jexpress.resonalis.com`, which passes it to your open, authorized J-Express tab. The tab computes the answer and the result travels back the same way to Claude. Depending on the tool, results contain dataset summaries, quality statistics, bounded slices of matrix values, row or column labels, analysis results or view images.

The plugin itself runs no local code, installs no packages and contacts no other service. Datasets are locked against writes by default. Tools that change data create new child datasets and need an explicit unlock and confirmation; the skills tell Claude to ask you before doing either.

See the [privacy policy](PRIVACY.md) for what the server stores and for how long.

## Support

J-Express and this plugin are provided by Resonalis. Contact: contact@resonalis.com.

## License

Apache-2.0. See [LICENSE](LICENSE).
