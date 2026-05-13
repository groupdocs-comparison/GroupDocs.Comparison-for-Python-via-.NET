from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def hide_revisions():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        options = CompareOptions()
        options.show_revisions = False
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    hide_revisions()