from groupdocs.comparison import Comparer

def list_changes():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        comparer.compare()
        for change in comparer.get_changes():
            print(f"Type: {change.type}, Text: {change.text}")

if __name__ == "__main__":
    list_changes()