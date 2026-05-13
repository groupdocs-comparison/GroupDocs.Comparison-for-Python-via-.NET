from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def ignore_word_track_changes():
    with Comparer("./source-with-revisions.docx") as comparer:
        comparer.add("./target.docx")
        options = CompareOptions()
        options.word_track_changes = False
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    ignore_word_track_changes()