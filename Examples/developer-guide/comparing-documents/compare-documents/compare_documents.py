from groupdocs.comparison import Comparer

def compare_documents():
    # Initialize Comparer with the source file path
    with Comparer("./source.docx") as comparer:
        # Add the target file and run the comparison
        comparer.add("./target.docx")
        comparer.compare("./result.docx")

if __name__ == "__main__":
    compare_documents()