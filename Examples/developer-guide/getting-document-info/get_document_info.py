from groupdocs.comparison import Comparer

def get_document_info():
    with Comparer("./source.docx") as comparer:
        info = comparer.source.get_document_info()
        print(f"File type: {info.file_type.file_format}")
        print(f"Number of pages: {info.page_count}")
        print(f"Document size: {info.size} bytes")
        print("\nDocument info extracted successfully.")

if __name__ == "__main__":
    get_document_info()