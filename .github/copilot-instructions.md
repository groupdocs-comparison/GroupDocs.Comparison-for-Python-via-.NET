# GitHub Copilot instructions — GroupDocs.Comparison for Python via .NET

This repository holds runnable Python examples for **GroupDocs.Comparison for Python via .NET**, the on-premise document comparison SDK.

GroupDocs.Comparison for Python via .NET is a document comparison API that programmatically compares 50+ document formats (Word, PDF, Excel, PowerPoint and more), detects changes, and produces a result document with highlighted differences.

> This repo ships a detailed `AGENTS.md` (the same reference bundled inside the wheel) with canonical imports, the full API surface, licensing, and troubleshooting. Prefer it as the authoritative reference; this file is a short summary.

## Install

```bash
pip install groupdocs-comparison-net
```

PyPI package: `groupdocs-comparison-net`. **Python** 3.5+ | **Platforms**: Windows, Linux, macOS. The wheel bundles the .NET runtime (no separate .NET install on Windows).

## Minimal working example

```python
from groupdocs.comparison import Comparer

with Comparer("source.docx") as comparer:
    comparer.add("target.docx")
    comparer.compare("result.docx")
```

- `Comparer(source)` — source path (positional), a stream via `document=...`, or a folder via `folder_path=...`.
- `comparer.add(target)` — add a target; call repeatedly for multi-document comparison.
- `comparer.compare(output[, options])` — run and write the result. Call `compare()` with no args before `get_changes()` to inspect changes without writing output.

Set a license (optional; trial mode otherwise):

```python
from groupdocs.comparison import License
License().set_license("path/to/license.lic")
```

Or auto-apply via `export GROUPDOCS_LIC_PATH="path/to/license.lic"`. Free temporary license: https://purchase.groupdocs.com/temporary-license/

## Common pitfalls

- **Package name vs import:** install `groupdocs-comparison-net`, but import from `groupdocs.comparison`.
- **Native deps on Linux/macOS:** `apt install libgdiplus libfontconfig1 ttf-mscorefonts-installer` (Linux) / `brew install mono-libgdiplus` (macOS). Windows needs nothing extra.
- **Properties are `snake_case`** (auto-mapped to .NET PascalCase); enums are case-insensitive (`FileType.DOCX`).
- **Use a `with` block** so native resources are released (or call `dispose()`).
- Without a license, output carries an evaluation watermark and is capped at the first two pages.

## SDK, not Cloud or MCP

- This is the **local/on-premise SDK** (`groupdocs-comparison-net`) — documents are processed locally via the bundled .NET runtime.
- **GroupDocs.Comparison Cloud** is a separate REST API product with different SDK packages — do not mix its classes with this SDK.
- The **MCP server** is a separate project: https://github.com/groupdocs-comparison/GroupDocs.Comparison.Mcp

## Links

- Docs: https://docs.groupdocs.com/comparison/python-net/
- API reference: https://reference.groupdocs.com/comparison/python-net/
- Supported formats: https://docs.groupdocs.com/comparison/python-net/supported-document-formats/
- How-to articles (blog): https://blog.groupdocs.com/categories/groupdocs.comparison-product-family/
