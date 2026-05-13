from groupdocs.comparison import Comparer
from groupdocs.comparison import Color
from groupdocs.comparison.options import CompareOptions, StyleSettings


def customize_changes_styles():
    options = CompareOptions()

    inserted = StyleSettings()
    inserted.font_color = Color.from_name("green")
    inserted.highlight_color = Color.from_name("red")
    inserted.is_underline = True
    inserted.is_bold = True
    options.inserted_item_style = inserted

    deleted = StyleSettings()
    deleted.font_color = Color.from_name("brown")
    deleted.highlight_color = Color.from_name("azure")
    deleted.is_strikethrough = True
    options.deleted_item_style = deleted

    changed = StyleSettings()
    changed.font_color = Color.from_name("firebrick")
    changed.highlight_color = Color.from_name("crimson")
    changed.is_italic = True
    options.changed_item_style = changed

    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    customize_changes_styles()