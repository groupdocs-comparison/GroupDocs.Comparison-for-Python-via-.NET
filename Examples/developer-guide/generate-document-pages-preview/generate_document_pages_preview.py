from groupdocs.comparison import Comparer
from groupdocs.comparison.options import PreviewOptions, PreviewFormats


def create_page_stream(page_number):
    # Return a writable stream — GroupDocs.Comparison writes the rendered page into it.
    return open(f"./page-{page_number}.png", "wb")


def release_page_stream(page_number):
    # The stream returned from create_page_stream has already been flushed and
    # closed by .NET. This hook is for any per-page bookkeeping you want to do.
    pass


def generate_document_pages_preview():
    with Comparer("./source.docx") as comparer:
        preview_options = PreviewOptions(create_page_stream, release_page_stream)
        preview_options.preview_format = PreviewFormats.PNG
        preview_options.page_numbers = [1, 2, 3]
        comparer.source.generate_preview(preview_options)

if __name__ == "__main__":
    generate_document_pages_preview()