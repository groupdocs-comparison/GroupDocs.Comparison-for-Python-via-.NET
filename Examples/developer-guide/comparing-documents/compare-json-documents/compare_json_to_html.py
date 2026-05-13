import io

from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def compare_json_to_html():
    options = CompareOptions()
    options.generate_summary_page = True

    # NOTE: HTML output via a file path triggers a self-collision inside the
    # GroupDocs.Comparison engine — Aspose.Html.HTMLDocument.Save re-opens the
    # destination path while the engine still holds it open, raising
    # `The process cannot access the file ... because it is being used by
    # another process`. The same happens when a FileStream is passed in (the
    # engine reads its Name and re-opens the path). Routing the output through
    # an in-memory BytesIO and writing to disk from Python avoids the path
    # entirely. See repro: C:\repository\groupdocs\issues\comparison-net\file-remain-open
    buffer = io.BytesIO()
    with Comparer("./source.json") as comparer:
        comparer.add("./target.json")
        comparer.compare(buffer, options)

    with open("./result_html.html", "wb") as f:
        f.write(buffer.getvalue())

if __name__ == "__main__":
    compare_json_to_html()
