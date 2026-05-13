from groupdocs.comparison import Comparer

def get_list_of_changes_stream():
    with open("./source.docx", "rb") as source_stream, \
         open("./target.docx", "rb") as target_stream:
        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare()
            for change in comparer.get_changes():
                print(f"Type: {change.type}, Page: {change.page_info.page_number}, Id: {change.id}, Text: {change.text}")

if __name__ == "__main__":
    get_list_of_changes_stream()