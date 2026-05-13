from groupdocs.comparison import Comparer, Color
from groupdocs.comparison.options import CompareOptions, StyleSettings


def compare_multiple_documents_settings():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target1.docx")
        comparer.add("./target2.docx")
        comparer.add("./target3.docx")

        options = CompareOptions()
        options.inserted_item_style = StyleSettings()
        options.inserted_item_style.font_color = Color.from_name("yellow")

        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    compare_multiple_documents_settings()