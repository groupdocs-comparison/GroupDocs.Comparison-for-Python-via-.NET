from groupdocs.comparison import Comparer
from groupdocs.comparison.options import LoadOptions

def load_custom_fonts():
    load_options = LoadOptions()
    load_options.font_directories.append("./fonts/")

    with Comparer("./source.docx", load_options) as comparer:
        comparer.add("./target.docx", load_options)
        comparer.compare("./result.docx")

if __name__ == "__main__":
    load_custom_fonts()