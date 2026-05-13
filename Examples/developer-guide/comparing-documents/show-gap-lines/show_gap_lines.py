from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def show_gap_lines():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        options = CompareOptions()
        options.show_inserted_content = False
        options.show_deleted_content = False
        options.leave_gaps = True
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    show_gap_lines()