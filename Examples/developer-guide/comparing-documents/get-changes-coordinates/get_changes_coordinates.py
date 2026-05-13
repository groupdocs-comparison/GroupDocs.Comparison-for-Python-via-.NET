from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def get_changes_coordinates():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        options = CompareOptions()
        options.calculate_coordinates = True
        comparer.compare(options)
        for change in comparer.get_changes():
            print(f"Type: {change.type}, X: {change.box.x}, Y: {change.box.y}, Text: {change.text}")

if __name__ == "__main__":
    get_changes_coordinates()