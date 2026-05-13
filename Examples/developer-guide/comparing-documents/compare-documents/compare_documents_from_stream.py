from groupdocs.comparison import Comparer

def compare_documents_from_stream():
    # Open the source and target as binary streams
    with open("./source.docx", "rb") as source_stream, \
         open("./target.docx", "rb") as target_stream:
        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare("./result.docx")

if __name__ == "__main__":
    compare_documents_from_stream()