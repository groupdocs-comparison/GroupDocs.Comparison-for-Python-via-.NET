# Documents Comparison Python API

[![Product Page](https://img.shields.io/badge/Product%20Page-2865E0?style=for-the-badge&logo=appveyor&logoColor=white)](https://products.groupdocs.com/comparison/python-net/) 
[![Docs](https://img.shields.io/badge/Docs-2865E0?style=for-the-badge&logo=Hugo&logoColor=white)](https://docs.groupdocs.com/comparison/python-net/) 
[![Demos](https://img.shields.io/badge/Demos-2865E0?style=for-the-badge&logo=appveyor&logoColor=white)](https://products.groupdocs.app/comparison/family) 
[![API Reference](https://img.shields.io/badge/API%20Reference-2865E0?style=for-the-badge&logo=html5&logoColor=white)](https://reference.groupdocs.com/comparison/) 
[![Blog](https://img.shields.io/badge/Blog-2865E0?style=for-the-badge&logo=WordPress&logoColor=white)](https://blog.groupdocs.com/category/comparison/) 
[![Search](https://img.shields.io/badge/Search-2865E0?style=for-the-badge&logo=searchengin&logoColor=white)](https://search.groupdocs.com/) 
[![Free Support](https://img.shields.io/badge/Free%20Support-2865E0?style=for-the-badge&logo=Discourse&logoColor=white)](https://forum.groupdocs.com/c/comparison) 
[![Temporary License](https://img.shields.io/badge/Temporary%20License-2865E0?style=for-the-badge&logo=rocket&logoColor=white)](https://purchase.groupdocs.com/temporary-license)


## Powerful Python API for File Comparison

[**GroupDocs.Comparison for Python via .NET**](https://products.groupdocs.com/comparison/python-net/) lets you easily **compare Word, Excel, PDF, PowerPoint, images, HTML, and more** directly from Python. It detects differences at **paragraph, word, character, and formatting levels** and produces clear visual or textual comparison results.

Build Python applications that **highlight changes between document versions, verify content, and ensure document integrity** with no external dependencies required.

## Quick start 

Compare two Word files in Python:

```python
from groupdocs.comparison import Comparer

with Comparer("source.docx") as comparer:
    comparer.add("target.docx")
    comparer.compare("result.docx")

print("Comparison complete. Output saved as result.docx")
```

**Results at glance:**

[![source_target_files](https://raw.githubusercontent.com/groupdocs/groupdocs.github.io/master/img/pypi/groupdocs-comparison/files_to_compare.png)](https://pypi.org/project/groupdocs-comparison-net/)

**Sample result file:**

[![result](https://raw.githubusercontent.com/groupdocs/groupdocs.github.io/master/img/pypi/groupdocs-comparison/result.png)](https://pypi.org/project/groupdocs-comparison-net/)

GroupDocs.Comparison highlights detected changes with different colors from the settings

## Comparison API Features

**GroupDocs.Comparison for Python via .NET** provides a comprehensive API to compare, analyze, and process document differences across multiple file formats:

- [**Accurate and reliable document comparison**](https://docs.groupdocs.com/comparison/python-net/compare-documents/) Detect changes in text, formatting, styles, images, tables, and document structure with precise highlighting for quick review.
- [**Manage detected changes**](https://docs.groupdocs.com/comparison/python-net/accept-or-reject-detected-changes/) lets you programmatically accept or reject individual changes before producing the final result.
- [**Compare PDF documents**](https://docs.groupdocs.com/comparison/python-net/compare-pdf-documents/) Compare PDF documents with high accuracy, including document structures like tables, text fields, images
- [**Obtain changes as an object model**](https://docs.groupdocs.com/comparison/python-net/get-result-document-object/) Get comparison result as an object model in Python
- [**Compare Multiple Documents**](https://docs.groupdocs.com/comparison/python-net/compare-multiple-documents-with-specific-compare-settings/) Compare multiple documents with specific compare settings.
- [**Document Metadata Management**](https://docs.groupdocs.com/comparison/python-net/set-document-metadata-on-save/) Set metadata in output documents from source, target, or custom values to ensure consistent and customizable metadata during comparison operations.

## Installation

### Quick Install:

```bash
pip install groupdocs-comparison-net
# or upgrade
pip install --upgrade groupdocs-comparison-net
```

### Manual Installation
1. Download the package for your OS from [GroupDocs Releases](https://releases.groupdocs.com/comparison/python-net/):
   - **Windows 64-bit:** `*amd64.whl`
   - **Linux 64-bit:** `*arm64.whl` 
   - **macOS Intel:** `*x86_64.whl`

2. Copy the downloaded file to your project folder

3. Install using pip:
   ```bash
   pip install downloaded_file.whl
   ```

## Supported Microsoft Office Formats

**Microsoft Word:** DOC, DOCM, DOCX, DOT, DOTM, DOTX\
**Microsoft Excel:** XLS, XLT, XLSX, XLTM, XLSB, XLSM, XLSX, CSV\
**Microsoft PowerPoint:** POT, POTX, PPS, PPSX, PPTX, PPT\
**Microsoft OneNote:** ONE\
**Microsoft Visio:** VSDX, VSD, VSS, VST, VDX

## Other Supported Formats

**OpenDocument:** ODT, ODP, OTP, ODS, OTT\
**Fixed Layout:** PDF\
**AutoCAD:** DWG, DXF\
**Email:** EML, EMLX, MSG\
**Images:** BMP, GIF, JPG, JPEG, PNG\
**Web:** HTM, HTML, MHT, MHTML \
**Text:** RTF, TXT\
**eBook:** MOBI, DjVu\
**Medical Imaging:** DCM\
**Programming Language:** CS, JAVA, CPP, JS, PY, RB 

See the [full list of supported formats](https://docs.groupdocs.com/comparison/python-net/supported-document-formats/).

## Usage Scenarios

- Compare contract versions in [**PDF or DOCX**](https://blog.groupdocs.com/comparison/compare-pdfs-using-python/).  
- Verify spreadsheet changes in **Excel XLSX** files including Charts.  
- Detect formatting edits in **PowerPoint** presentations.  
- [**Mastering JSON**](https://blog.groupdocs.com/comparison/compare-pdfs-using-python/) contractors comparison
- Highlight pixel-level differences in **PNG or TIFF images**.  
- Automate **QA document review workflows** in Python apps.


## Compare PDF Files and get list of changes via Python

Produce a **merged PDF file** with inline diff markers:
- Deleted content is wrapped in `[ ]`
- Inserted content is wrapped in `( )`

```python
import groupdocs.comparison as gc
from groupdocs.comparison.options import CompareOptions

source_path = "source.pdf"
target_path = "target.pdf"
result_path = "result.pdf"

options = CompareOptions()
options.detect_style_changes = True
options.show_deleted_content = True

with gc.Comparer(source_path) as comparer:
    comparer.add(target_path)
    comparer.compare(result_path, options)
```

## Compare multiple documents

The following code snippet shows how to compare several password-protected documents from a local disk(from stream also available).
**Note:** This feature is available only for Word documents, PowerPoint, and Open Document presentations.

```python
import groupdocs.comparison as gc

def compare_multiple_documents(source_path, target_paths, result_path, output_directory, output_file_name):

    # Initialize the comparer with the source file
    comparer = gc.Comparer(source_path)

    # Add target files
    for target_path in target_paths:
        comparer.add(target_path)

    # Set comparison options and save options
    save_options = gc.options.SaveOptions()
    compare_options = gc.options.CompareOptions()

    # Perform the compare operation and save the result
    comparer.compare(output_file_name, save_options, compare_options)

    print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")
```

## Get file info for the DOCX file with Python

You can use **GroupDocs.Comparison for Python via .NET** to retrieve detailed metadata about a document before or after comparison.  
The `get_document_info()` method provides information such as file type, total number of pages, file size, and page dimensions.  
This can be helpful for validating files, displaying document details to users, or logging document statistics.

```python
import groupdocs.comparison as gc

source_path = "source.docx"

# Initialize the comparer with the source DOCX file
with gc.Comparer(source_path) as comparer:
    # Retrieve document metadata such as page count and size
    info = comparer.source.get_document_info()

    # Iterate through each page to display detailed information
    for i, page in enumerate(info.pages_info, start=1):
        print(
            f"\nPage number: {i}\n"
            f"File type: {info.file_type}\n"
            f"Number of pages: {info.page_count}\n"
            f"Document size: {info.size} bytes\n"
            f"Width: {page.width}\n"
            f"Height: {page.height}"
        )

```

> GroupDocs.Comparison for Python requires you to use python programming language. For Node.js, Java and .NET languages, we recommend you get [GroupDocs.Comparison for Node.js](https://products.groupdocs.com/comparison/nodejs-java/), [GroupDocs.Comparison for Java](https://products.groupdocs.com/comparison/java/) and [GroupDocs.Comparison for .NET](https://products.groupdocs.com/comparison/net/), respectively.

[![Product Page](https://img.shields.io/badge/Product%20Page-2865E0?style=for-the-badge&logo=appveyor&logoColor=white)](https://products.groupdocs.com/comparison/python-net/) 
[![Docs](https://img.shields.io/badge/Docs-2865E0?style=for-the-badge&logo=Hugo&logoColor=white)](https://docs.groupdocs.com/comparison/python-net/) 
[![Demos](https://img.shields.io/badge/Demos-2865E0?style=for-the-badge&logo=appveyor&logoColor=white)](https://products.groupdocs.app/comparison/family) 
[![API Reference](https://img.shields.io/badge/API%20Reference-2865E0?style=for-the-badge&logo=html5&logoColor=white)](https://reference.groupdocs.com/comparison/) 
[![Blog](https://img.shields.io/badge/Blog-2865E0?style=for-the-badge&logo=WordPress&logoColor=white)](https://blog.groupdocs.com/category/comparison/) 
[![Search](https://img.shields.io/badge/Search-2865E0?style=for-the-badge&logo=searchengin&logoColor=white)](https://search.groupdocs.com/) 
[![Free Support](https://img.shields.io/badge/Free%20Support-2865E0?style=for-the-badge&logo=Discourse&logoColor=white)](https://forum.groupdocs.com/c/comparison) 
[![Temporary License](https://img.shields.io/badge/Temporary%20License-2865E0?style=for-the-badge&logo=rocket&logoColor=white)](https://purchase.groupdocs.com/temporary-license)
