<!-- generator:skip -->
# GroupDocs.Comparison for Python via .NET -- AGENTS.md

> Instructions for AI agents working with this package.

Compare documents and detect text, style, and formatting changes -- Word, PDF, Excel, PowerPoint, ODT, HTML, images, and more. Includes accept/reject workflows and multi-source comparison.

## Install

```bash
pip install groupdocs-comparison-net
```

**Python**: 3.5 - 3.14 | **Platforms**: Windows, Linux, macOS

## Resources

| Resource | URL |
|---|---|
| Documentation | https://docs.groupdocs.com/comparison/python-net/ |
| LLM-optimized docs | https://docs.groupdocs.com/comparison/python-net/llms-full.txt |
| API reference | https://reference.groupdocs.com/comparison/python-net/ |
| Code examples | https://docs.groupdocs.com/comparison/python-net/developer-guide/ |
| Release notes | https://releases.groupdocs.com/comparison/python-net/release-notes/ |
| PyPI | https://pypi.org/project/groupdocs-comparison-net/ |
| Free support forum | https://forum.groupdocs.com/c/comparison/ |
| Temporary license | https://purchase.groupdocs.com/temporary-license |

## MCP Server

If your environment has MCP configured, you can connect your AI tool to the GroupDocs documentation server for on-demand API lookups:

```json
{
  "mcpServers": {
    "groupdocs-docs": {
      "url": "https://docs.groupdocs.com/mcp"
    }
  }
}
```

Works with Claude Code (`~/.claude/settings.json`), Cursor (`.cursor/mcp.json`), VS Code Copilot (`.vscode/mcp.json`), and any MCP-compatible client. If MCP is unavailable, fall back to the LLM-optimized docs URL above and this file -- both are shipped inside the wheel.

## Imports

```python
from groupdocs.comparison import License, Metered, Comparer, ComparerSettings, Document, Color
from groupdocs.comparison.common.exceptions import ComparisonException, DocumentComparisonException
from groupdocs.comparison.interfaces import IDocumentInfo
from groupdocs.comparison.localization import SupportedLocales
from groupdocs.comparison.logging import ConsoleLogger
from groupdocs.comparison.options import (
    ApplyChangeOptions, CompareOptions, GetChangeOptions,
    LoadOptions, SaveOptions, PreviewOptions,
    CalculateCoordinatesModeEnumeration, ChangeType, ComparisonDisplayMode,
    DetalisationLevel, FolderComparisonExtension, ImagesInheritance,
    MetadataType, PaperSize, PasswordSaveOption, PreviewFormats,
    StyleSettings, OriginalSize, DiagramMasterSetting, FileAuthorMetadata,
    IgnoreChangeSensitivitySettings, PagesSetup, PdfCompareOptions,
    PreviewResolution, Size, WordCompareOptions,
    Color,  # re-exported from groupdocs.pydrawing for styling
)
from groupdocs.comparison.result import (
    ChangeInfo, ComparisonAction, FileType,
    PageInfo, Rectangle, StyleChangeInfo,
)
from groupdocs.comparison.words.revision import (
    ApplyRevisionOptions, RevisionAction, RevisionHandler,
    RevisionInfo, RevisionType,
)
```

## Quick Start

```python
from groupdocs.comparison import Comparer

with Comparer("source.docx") as comparer:
    comparer.add("target.docx")
    comparer.compare("result.docx")
```

## Compare with Options

```python
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

with Comparer("source.docx") as comparer:
    comparer.add("target.docx")
    options = CompareOptions()
    options.sensitivity_of_comparison = 75
    options.detect_style_changes = True
    options.generate_summary_page = True
    comparer.compare("result.docx", options)
```

**Comparer constructor.** `Comparer(file_path=None, folder_path=None, compare_options=None, load_options=None, settings=None, document=None)` accepts kwargs. Pass a path string positionally, or a stream as `document=...`, or a folder via `folder_path=...`:

```python
from groupdocs.comparison import Comparer, ComparerSettings
from groupdocs.comparison.logging import ConsoleLogger
from groupdocs.comparison.options import LoadOptions

settings = ComparerSettings()
settings.logger = ConsoleLogger()

load = LoadOptions(); load.password = "1234"
with Comparer("protected.docx", load_options=load, settings=settings) as comparer:
    comparer.add("target.docx", load_options=load)
    comparer.compare("result.docx")
```

## Get Detected Changes

```python
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import ChangeType

with Comparer("source.docx") as comparer:
    comparer.add("target.docx")
    comparer.compare()                       # call with no args before get_changes()
    for change in comparer.get_changes():
        print(f"[{change.type}] {change.text}")

# Filter by change type
with Comparer("source.docx") as comparer:
    comparer.add("target.docx")
    comparer.compare()
    inserted = comparer.get_changes(filter=ChangeType.INSERTED)
```

## Accept / Reject Individual Changes

```python
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import ApplyChangeOptions
from groupdocs.comparison.result import ComparisonAction

with Comparer("source.docx") as comparer:
    comparer.add("target.docx")
    comparer.compare()
    changes = comparer.get_changes()
    # Reject the first detected change
    changes[0].comparison_action = ComparisonAction.REJECT
    apply_opts = ApplyChangeOptions()
    apply_opts.changes = changes
    comparer.apply_changes("result.docx", apply_opts)
```

## Multi-Source Comparison

```python
from groupdocs.comparison import Comparer

with Comparer("source.docx") as comparer:
    comparer.add("target1.docx")
    comparer.add("target2.docx")
    comparer.add("target3.docx")
    comparer.compare("result.docx")
```

## Customise Change Styling (colours)

`StyleSettings` controls how inserted / deleted / changed regions look in the result document. Colour properties accept anything that looks like a colour — a `Color` struct, an `(r, g, b)` or `(r, g, b, a)` tuple, a packed-ARGB `int`, a `'#RRGGBB'` / `'#AARRGGBB'` string, or a named colour string.

```python
from groupdocs.comparison import Comparer, Color
from groupdocs.comparison.options import CompareOptions, StyleSettings

with Comparer("source.docx") as comparer:
    comparer.add("target.docx")
    options = CompareOptions()
    options.inserted_item_style = StyleSettings()
    options.inserted_item_style.font_color = Color.from_name("firebrick")
    options.deleted_item_style = StyleSettings()
    options.deleted_item_style.font_color = (200, 100, 50)        # RGB tuple
    options.deleted_item_style.highlight_color = "#FFFF00"        # hex string
    options.changed_item_style = StyleSettings()
    options.changed_item_style.font_color = 0xFF0000FF            # packed ARGB
    comparer.compare("result.docx", options)
```

`Color` is also importable from `groupdocs.comparison.options` (next to `StyleSettings`) or directly from `groupdocs.pydrawing`. Case-insensitive named-colour access works too (`Color.red`, `Color.Red`, `Color.RED`, `Color.light_blue`).

## Render Page Previews

`Document.generate_preview(PreviewOptions(...))` produces per-page PNG/JPEG/BMP previews. `PreviewOptions` accepts plain Python callables for the stream factories — no adapter classes needed.

```python
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import PreviewOptions, PreviewFormats

def create_page_stream(page_number: int):
    # Return a writable stream — .NET writes the rendered page into it.
    return open(f"page-{page_number}.png", "wb")

def release_page_stream(page_number: int):
    # Called after .NET is done with the stream. The stream you returned
    # from create_page_stream is already flushed/closed by .NET.
    pass

with Comparer("source.docx") as comparer:
    preview = PreviewOptions(create_page_stream, release_page_stream)
    preview.preview_format = PreviewFormats.PNG
    preview.page_numbers = [1, 2, 3]
    comparer.source.generate_preview(preview)
```

`PreviewOptions(create_page_stream)` is also valid — pass just the create callback and omit the release one.

## Get Change Coordinates

When `CompareOptions.calculate_coordinates = True`, each `ChangeInfo.box` returns a `Rectangle` with snake_case `.x / .y / .width / .height` accessors (no PascalCase-dict gymnastics):

```python
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

with Comparer("source.docx") as comparer:
    comparer.add("target.docx")
    options = CompareOptions()
    options.calculate_coordinates = True
    comparer.compare("result.docx", options)
    for change in comparer.get_changes():
        b = change.box
        print(f"({b.x:.0f}, {b.y:.0f}) {b.width:.0f}x{b.height:.0f} — {change.text!r}")
```

## Password-Protected Documents

```python
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import LoadOptions, SaveOptions

src_load = LoadOptions(); src_load.password = "1234"
tgt_load = LoadOptions(); tgt_load.password = "5678"
save_opts = SaveOptions(); save_opts.password = "out-secret"

with Comparer("protected_source.docx", load_options=src_load) as comparer:
    comparer.add("protected_target.docx", load_options=tgt_load)
    comparer.compare("result.docx",
                     compare_options=None, save_options=save_opts)
```

## Compare from Stream

```python
import io
from groupdocs.comparison import Comparer

with open("source.docx", "rb") as src, open("target.docx", "rb") as tgt:
    with Comparer(src) as comparer:
        comparer.add(tgt)
        comparer.compare("result.docx")

# Or from in-memory bytes
src_buf = io.BytesIO(source_bytes)
tgt_buf = io.BytesIO(target_bytes)
with Comparer(src_buf) as comparer:
    comparer.add(tgt_buf)
    comparer.compare("result.docx")
```

## Get Document Info

```python
from groupdocs.comparison import Comparer

with Comparer("document.docx") as comparer:
    info = comparer.source.get_document_info()
    print(f"Pages: {info.page_count}, Size: {info.size}")
```

## Command Line

The wheel installs a `groupdocs-comparison` console script (also reachable via `python -m groupdocs.comparison`).

```bash
groupdocs-comparison compare SOURCE TARGET OUTPUT [flags]
groupdocs-comparison info FILE
groupdocs-comparison list-formats
groupdocs-comparison --license PATH ...        # apply a license first
groupdocs-comparison --version
groupdocs-comparison --help
python -m groupdocs.comparison --version       # equivalent module form
```

`compare` flags:

| Flag | Type | Effect |
|---|---|---|
| `--password` | str | Password for protected source/target documents |
| `--output-password` | str | Password applied to the resultant document |
| `--sensitivity` | int (0-100) | Sensitivity of comparison |
| `--detect-style-changes` | flag | Detect bold / italic / colour changes |
| `--mark-changed-content` | flag | Mark changed content in the result |
| `--compare-bookmarks` | flag | Include bookmark comparison |
| `--generate-summary-page` | flag | Append a summary page with statistics |
| `--show-revisions` | flag | Show Word track-changes revisions |

**Exit codes.** `0` success · `2` user error (missing input) · `1` runtime error (.NET exception body printed).

**Limits.** The CLI is a thin shim over the Python API for the common case. Drop into Python for: multi-target compare in one Comparer, in-memory streams (`io.BytesIO`), accept/reject individual changes (`apply_changes`), folder comparison, custom logging or comparer settings, revision handlers.

## Licensing

```python
from groupdocs.comparison import License

# From file
License().set_license("path/to/license.lic")

# From stream
with open("license.lic", "rb") as f:
    License().set_license(f)
```

Or auto-apply: `export GROUPDOCS_LIC_PATH="path/to/license.lic"`

**Evaluation vs licensed.** Without a license the library still runs, but PDF output carries an evaluation watermark stamp and non-PDF targets show an equivalent evaluation mark; there is also a page/document count cap. Set `GROUPDOCS_LIC_PATH` (or call `License().set_license(...)`) and re-run to clear both. A 30-day full license is free: https://purchase.groupdocs.com/temporary-license

## API Reference

### Comparer

| Method | Returns | Description |
|---|---|---|
| `__init__(file_path=None, folder_path=None, compare_options=None, load_options=None, settings=None, document=None)` | | Open a source. Pass path positionally, or `folder_path=` / `document=` (stream) by kwarg |
| `add(file_path=None, compare_options=None, load_options=None, document=None)` | `None` | Register a target for comparison. Call repeatedly for multi-source |
| `compare(file_path=None, stream=None, compare_options=None, save_options=None)` | `Document` | Run the comparison. Call with no args before `get_changes()` to materialise without writing output |
| `get_changes(get_change_options=None, filter=None)` | `list[ChangeInfo]` | Retrieve detected changes after `compare()` |
| `apply_changes(file_path=None, apply_change_options=None, stream=None, save_options=None)` | `None` | Re-emit the result honoring per-change `comparison_action` |
| `compare_directory(file_path=None, compare_options=None)` | `None` | Folder-level compare (set `compare_options.directory_compare = True`) |
| `get_result_string()` | `str` | Result document as text |
| `get_result_document_stream()` | `Stream` | Result document as a stream |
| `dispose()` | `None` | Release native resources (use a `with` block instead when possible) |

Properties: `source: Document`, `targets: list[Document]`, `result: Document`, `source_folder: str`, `target_folder: str`.

### CompareOptions

| Property | Type | Writable |
|---|---|---|
| `paper_size` | `PaperSize` | yes |
| `show_deleted_content` | `bool` | yes |
| `show_inserted_content` | `bool` | yes |
| `generate_summary_page` | `bool` | yes |
| `extended_summary_page` | `bool` | yes |
| `show_only_summary_page` | `bool` | yes |
| `detect_style_changes` | `bool` | yes |
| `mark_nested_content` | `bool` | yes |
| `calculate_coordinates` | `bool` | yes |
| `calculate_coordinates_mode` | `CalculateCoordinatesModeEnumeration` | yes |
| `header_footers_comparison` | `bool` | yes |
| `detalisation_level` | `DetalisationLevel` | yes |
| `mark_changed_content` | `bool` | yes |
| `inserted_item_style` | `StyleSettings` | yes |
| `deleted_item_style` | `StyleSettings` | yes |
| `changed_item_style` | `StyleSettings` | yes |
| `mark_line_breaks` | `bool` | yes |
| `compare_images_pdf` | `bool` | yes |
| `images_inheritance_mode` | `ImagesInheritance` | yes |
| `compare_bookmarks` | `bool` | yes |
| `compare_variable_property` | `bool` | yes |
| `compare_document_property` | `bool` | yes |
| `word_track_changes` | `bool` | yes |
| `show_only_changed` | `bool` | yes |
| `directory_compare` | `bool` | yes |
| `user_master_path` | `str` | yes |
| `folder_comparison_extension` | `FolderComparisonExtension` | yes |
| `revision_author_name` | `str` | yes |
| `sensitivity_of_comparison` | `int` | yes |
| `sensitivity_of_comparison_for_tables` | `int?` | yes |
| `ignore_change_settings` | `IgnoreChangeSensitivitySettings` | yes |
| `words_separator_chars` | `Char[]` | yes |
| `password_save_option` | `PasswordSaveOption` | yes |
| `original_size` | `OriginalSize` | yes |
| `diagram_master_setting` | `DiagramMasterSetting` | yes |
| `show_revisions` | `bool` | yes |
| `leave_gaps` | `bool` | yes |

### LoadOptions

| Property | Type | Writable |
|---|---|---|
| `password` | `str` | yes |
| `font_directories` | `list` | yes |
| `load_text` | `bool` | yes |
| `file_type` | `FileType` | yes |

### SaveOptions

| Property | Type | Writable |
|---|---|---|
| `password` | `str` | yes |

### ApplyChangeOptions

| Property | Type | Writable |
|---|---|---|
| `changes` | `list[ChangeInfo]` | yes |
| `save_original_state` | `bool` | yes |

### ChangeInfo

| Property | Type | Description |
|---|---|---|
| `id` | `int` | Stable identifier for the change |
| `type` | `ChangeType` | INSERTED / DELETED / STYLE_CHANGED / etc. |
| `text` | `str` | Affected text |
| `author` | `str` | Original author (when available) |
| `comparison_action` | `ComparisonAction` | Set to ACCEPT / REJECT before `apply_changes()` |
| `box` | `Rectangle` | Coordinates if `calculate_coordinates=True` was set. Read via `change.box.x / .y / .width / .height` |
| `style_changes` | `list[StyleChangeInfo]` | Per-property style deltas |

## Key Patterns

- **Properties**: use `snake_case` -- auto-mapped to .NET `PascalCase`
- **Context managers**: `with Comparer(...) as x:` ensures resources are released
- **Streams**: pass `open("file", "rb")` or `io.BytesIO(data)` where .NET expects Stream
- **Stream write-back**: `BytesIO` objects are updated after .NET writes to them
- **Enums**: case-insensitive, lazy-loaded (e.g., `FileType.DOCX`)
- **Collections**: `for item in result` and `len(result)` work on .NET collections
- **Apply-changes flow**: `compare()` (no args) → `get_changes()` → set `comparison_action` per change → `apply_changes(out, ApplyChangeOptions(changes=...))`. Calling `compare(out)` with an output path skips the apply-changes step entirely.

## Platform Requirements

| Platform | Requirements |
|---|---|
| Windows | None |
| Linux | `apt install libgdiplus libfontconfig1 ttf-mscorefonts-installer` |
| macOS | `brew install mono-libgdiplus` |

## Troubleshooting

**`"Error occurred while converting document"` when comparing XLSX → XLSX** -- known upstream-side issue in `GroupDocs.Comparison.dll` SaveDocument step (reproduces in pure .NET, not a wrapper bug). DOCX/PDF/TXT/PPTX paths are unaffected. Track upstream for a fix; in the meantime convert to PDF or DOCX target instead.

**`Gdip` type initializer / `libgdiplus` DllNotFoundException on macOS Apple Silicon** -- `GroupDocs.Comparison.dll`'s PDF and image diff paths go through `System.Drawing.Common`, which fails to load `libgdiplus` on mac-arm64 even when the library is installed and individually loadable. DOCX/TXT/HTML/PPTX compares are unaffected. Workarounds: (a) compare to a non-rasterized target format like DOCX or HTML when possible; (b) run the comparison on macOS x64, Linux, or Windows where this code path works. Engine-side fix needed (drop `System.Drawing.Common` in favour of SkiaSharp / Aspose.Drawing, which other GroupDocs products already use cross-platform).

**`System.Drawing.Common is not supported`** -- install libgdiplus: `sudo apt install libgdiplus` (Linux) / `brew install mono-libgdiplus` (macOS)

**`Gdip` type initializer exception** -- outdated libgdiplus: `brew reinstall mono-libgdiplus` (macOS)

**Garbled text / missing fonts** -- install fonts: `sudo apt install ttf-mscorefonts-installer fontconfig && sudo fc-cache -f`

**`DllNotFoundException: libSkiaSharp`** -- stale system copy conflicts with bundled version. Rename it: `sudo mv /usr/local/lib/libSkiaSharp.dylib /usr/local/lib/libSkiaSharp.dylib.bak`

**`DOTNET_SYSTEM_GLOBALIZATION_INVARIANT` errors** -- do NOT set this. Install ICU: `sudo apt install libicu-dev`

**`TypeLoadException`** -- reinstall: `pip install --force-reinstall groupdocs-comparison-net`

**Still stuck?** Post your question at https://forum.groupdocs.com/c/comparison/ -- the development team responds directly.
