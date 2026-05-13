from groupdocs.comparison import Comparer

def get_result_document_object():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        result_document = comparer.compare("./result.docx")
        for change in result_document.changes:
            print(f"Source text: {change.source_text}")
            print(f"Target text: {change.target_text}\n")

if __name__ == "__main__":
    get_result_document_object()