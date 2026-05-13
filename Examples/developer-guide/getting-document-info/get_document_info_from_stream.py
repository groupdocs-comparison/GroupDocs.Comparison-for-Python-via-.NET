from groupdocs.comparison import Comparer

def get_document_info_from_stream():
    with open("./source.docx", "rb") as source_stream:
        with Comparer(source_stream) as comparer:
            info = comparer.source.get_document_info()
            print(f"File type: {info.file_type.file_format}")
            print(f"Number of pages: {info.page_count}")
            print(f"Document size: {info.size} bytes")

if __name__ == "__main__":
    get_document_info_from_stream()