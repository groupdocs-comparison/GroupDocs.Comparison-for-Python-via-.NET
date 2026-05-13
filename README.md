# GroupDocs.Comparison for Python via .NET - Code Examples

[![banner](https://raw.githubusercontent.com/groupdocs/groupdocs.github.io/master/img/banners/groupdocs-comparison-python-net-banner.png)](https://releases.groupdocs.com/comparison/python-net/)

[Product Page](https://products.groupdocs.com/comparison/python-net/) | [Docs](https://docs.groupdocs.com/comparison/python-net/) | [Demos](https://products.groupdocs.app/comparison/family) | [API Reference](https://reference.groupdocs.com/comparison/python-net/) | [Blog](https://blog.groupdocs.com/category/comparison/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/comparison) | [Temporary License](https://purchase.groupdocs.com/temporary-license)

[GroupDocs.Comparison for Python via .NET](https://products.groupdocs.com/comparison/python-net/) is a document comparison API that detects differences between source and target files — text blocks, paragraphs, words, characters, tables, images, and shapes — across 50+ formats including DOCX, PDF, XLSX, PPTX, images, CAD, and email.

## Features

- **50+ Supported Formats**: Compare DOCX, PDF, XLSX, PPTX, images, CAD, email and many more file types.
- **Granular Change Detection**: Detect added, modified, styled, and deleted content at paragraph, word, and character levels.
- **Accept or Reject Changes**: Programmatically apply or reject detected changes and save the resulting document.
- **Multi-Document Comparison**: Compare a source document against multiple targets in a single operation.
- **Streams & Custom Sources**: Read inputs from file paths or streams; write results to either.
- **On-Premise**: No cloud or internet connection required.

## Supported File Formats

GroupDocs.Comparison for Python via .NET supports a wide range of file formats, including Word, Excel, PowerPoint, PDF, OpenDocument, Image, Email, and many others. See the [full list of supported formats](https://docs.groupdocs.com/comparison/python-net/supported-document-formats/) for details.

## Get Started

1. **Set Up Environment**: Ensure that [Python 3.5+](https://www.python.org/downloads/) is installed on your system.

2. **Get the Code**: Clone or download this repository.

   ```bash
   git clone git@github.com:groupdocs-comparison/GroupDocs.Comparison-for-Python-via-.NET.git
   ```

3. **Navigate to the `Examples` Folder**

   ```bash
   cd ./GroupDocs.Comparison-for-Python-via-.NET/Examples
   ```

4. **Install Package**: install dependencies with pip:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, download the platform-specific `.whl` file from the [GroupDocs Releases](https://releases.groupdocs.com/comparison/python-net/) website and install it directly (adjust the filename to your platform — `win_amd64`, `manylinux*_x86_64`, `macosx_*_arm64`, `macosx_*_x86_64`):

   ```bash
   pip install ./groupdocs_comparison_net-26.5.0-py3-none-win_amd64.whl
   ```

5. **Configure License (Optional)**: `run_all_examples.py` automatically applies a license when one is available, looking in two places:

   - The `GROUPDOCS_LIC_PATH` environment variable — set it to the absolute path of your `.lic` file (recommended).
   - Any `*.lic` file in the repository root.

   With a license applied, examples run with the full feature set; without one, output documents carry an evaluation watermark and are capped at the first two pages. Get a free 30-day [temporary license](https://purchase.groupdocs.com/temporary-license) for evaluation.

6. **Run the Examples**: To run all the examples, execute the following command:

   ```bash
   python ./run_all_examples.py
   ```

   You can also run individual examples by navigating to the folder containing the example script and running it. Output files are placed in the same folder as the script file.

## Run with Docker

The repository ships a `Dockerfile` that builds a Linux image with Python 3.13, the .NET runtime dependencies (`libicu-dev`), and the `groupdocs-comparison-net` package preinstalled.

```bash
# Build the image
docker build -t comparison-examples .

# Run unlicensed (evaluation mode)
docker run --rm comparison-examples

# Run with a license mounted from the host
docker run --rm \
    -v /path/to/license:/lic:ro \
    -e GROUPDOCS_LIC_PATH=/lic/your-license.lic \
    comparison-examples
```

On Windows with Git Bash, set `export MSYS_NO_PATHCONV=1` before `docker run` to prevent MSYS from rewriting the mounted license path.

## AI agents and LLM integration

The `groupdocs-comparison-net` wheel ships a bundled `AGENTS.md` reference for AI coding assistants (Claude Code, Cursor, GitHub Copilot in agent mode, and similar). Once the package is installed, the reference is discovered automatically at `groupdocs/comparison/AGENTS.md` — it covers canonical imports, quick-start usage, licensing, the API surface table, and troubleshooting.

For on-demand documentation lookups, combine the bundled `AGENTS.md` with the GroupDocs MCP server at `https://docs.groupdocs.com/mcp`. See the [AI agents and LLM integration](https://docs.groupdocs.com/comparison/python-net/agents-and-llm-integration/) page for the per-tool setup snippets.

## Continuous integration

The `.github/workflows/` directory contains the CI matrix that runs the full example suite on every push. The matrix is reproducible locally via the `Dockerfile` above.

## More Resources

Find additional details and examples in the [GroupDocs.Comparison for Python via .NET documentation](https://docs.groupdocs.com/comparison/python-net/).

We also offer **GroupDocs.Comparison** packages for other platforms:
* [**GroupDocs.Comparison for .NET**](https://products.groupdocs.com/comparison/net/)
* [**GroupDocs.Comparison for Java**](https://products.groupdocs.com/comparison/java/)

---

[Product Page](https://products.groupdocs.com/comparison/python-net/) | [Docs](https://docs.groupdocs.com/comparison/python-net/) | [Demos](https://products.groupdocs.app/comparison/family) | [API Reference](https://reference.groupdocs.com/comparison/python-net/) | [Blog](https://blog.groupdocs.com/category/comparison/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/comparison) | [Temporary License](https://purchase.groupdocs.com/temporary-license)
