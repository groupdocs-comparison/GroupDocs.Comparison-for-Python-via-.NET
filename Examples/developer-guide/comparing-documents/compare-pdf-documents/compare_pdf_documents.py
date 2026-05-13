from groupdocs.comparison import Comparer

def compare_pdf_documents():
    with Comparer("./source.pdf") as comparer:
        comparer.add("./target.pdf")
        comparer.compare("./result.pdf")

if __name__ == "__main__":
    compare_pdf_documents()