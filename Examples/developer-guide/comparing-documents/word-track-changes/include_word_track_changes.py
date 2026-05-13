from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def include_word_track_changes():
    with Comparer("./source-with-revisions.docx") as comparer:
        comparer.add("./target.docx")
        options = CompareOptions()
        options.word_track_changes = True
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    include_word_track_changes()