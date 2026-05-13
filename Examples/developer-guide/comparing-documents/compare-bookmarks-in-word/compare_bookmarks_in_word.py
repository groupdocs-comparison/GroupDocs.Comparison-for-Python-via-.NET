from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def compare_bookmarks_in_word():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        options = CompareOptions()
        options.compare_bookmarks = True
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    compare_bookmarks_in_word()