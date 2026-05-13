from groupdocs.comparison import Comparer

def compare_word_documents():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        comparer.compare("./result.docx")

if __name__ == "__main__":
    compare_word_documents()