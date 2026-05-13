from groupdocs.comparison import Comparer
from groupdocs.comparison.options import LoadOptions
from groupdocs.comparison.result import FileType

def specify_file_type_manually():
    load_options = LoadOptions()
    load_options.file_type = FileType.DOCX

    with Comparer("./source.docx", load_options) as comparer:
        comparer.add("./target.docx", load_options)
        comparer.compare("./result.docx")

if __name__ == "__main__":
    specify_file_type_manually()