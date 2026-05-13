from groupdocs.comparison import Comparer

def compare_documents_to_stream():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        with open("./result.docx", "wb") as out_stream:
            comparer.compare(out_stream)

if __name__ == "__main__":
    compare_documents_to_stream()