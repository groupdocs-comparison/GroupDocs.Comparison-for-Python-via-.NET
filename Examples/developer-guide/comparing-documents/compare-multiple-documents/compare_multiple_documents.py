from groupdocs.comparison import Comparer

def compare_multiple_documents():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target1.docx")
        comparer.add("./target2.docx")
        comparer.add("./target3.docx")
        comparer.compare("./result.docx")
        print("Documents compared successfully. Result saved to result.docx.")

if __name__ == "__main__":
    compare_multiple_documents()