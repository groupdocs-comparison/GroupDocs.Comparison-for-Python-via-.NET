from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def set_author_of_changes():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        options = CompareOptions()
        options.show_revisions = True
        options.word_track_changes = True
        options.revision_author_name = "New author"
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    set_author_of_changes()