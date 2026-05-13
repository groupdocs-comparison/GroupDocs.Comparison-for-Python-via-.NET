from groupdocs.comparison import Comparer
from groupdocs.comparison import Color
from groupdocs.comparison.options import CompareOptions, StyleSettings


def customize_changes_styles_stream():
    options = CompareOptions()
    options.inserted_item_style = StyleSettings()
    options.inserted_item_style.font_color = Color.from_name("green")
    options.inserted_item_style.is_underline = True

    options.deleted_item_style = StyleSettings()
    options.deleted_item_style.is_strikethrough = True

    options.changed_item_style = StyleSettings()
    options.changed_item_style.is_italic = True

    with open("./source.docx", "rb") as source_stream, \
         open("./target.docx", "rb") as target_stream, \
         open("./result.docx", "wb") as out_stream:
        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare(out_stream, options)

if __name__ == "__main__":
    customize_changes_styles_stream()