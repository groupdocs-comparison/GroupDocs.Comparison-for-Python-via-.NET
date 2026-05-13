from groupdocs.comparison import Comparer
from groupdocs.comparison import Color
from groupdocs.comparison.options import CompareOptions, StyleSettings


def set_shape_color_independently():
    options = CompareOptions()
    options.detect_style_changes = True
    options.mark_changed_content = True

    inserted = StyleSettings()
    inserted.font_color = Color.from_name("blue")
    inserted.shape_color = Color.from_name("purple")
    options.inserted_item_style = inserted

    deleted = StyleSettings()
    deleted.font_color = Color.from_name("red")
    deleted.shape_color = Color.from_name("orange")
    options.deleted_item_style = deleted

    changed = StyleSettings()
    changed.font_color = Color.from_name("green")
    changed.shape_color = Color.from_name("lightgreen")
    options.changed_item_style = changed

    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    set_shape_color_independently()