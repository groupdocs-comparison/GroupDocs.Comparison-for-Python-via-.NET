from groupdocs.comparison import Comparer

def get_list_of_changes():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        comparer.compare()
        for change in comparer.get_changes():
            print(f"Type: {change.type}, Page: {change.page_info.page_number}, Id: {change.id}, Text: {change.text}")

if __name__ == "__main__":
    get_list_of_changes()