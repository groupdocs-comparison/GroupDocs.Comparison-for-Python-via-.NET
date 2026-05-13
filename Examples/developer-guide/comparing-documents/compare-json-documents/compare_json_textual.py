from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def compare_json_textual():
    options = CompareOptions()
    options.detect_style_changes = True
    options.show_deleted_content = True

    with Comparer("./source.json") as comparer:
        comparer.add("./target.json")
        comparer.compare("./result_textual.json", options)

if __name__ == "__main__":
    compare_json_textual()