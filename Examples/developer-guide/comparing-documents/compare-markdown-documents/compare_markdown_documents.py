from groupdocs.comparison import Comparer

def compare_markdown_documents():
    with Comparer("./source.md") as comparer:
        comparer.add("./target.md")
        comparer.compare("./result.md")

if __name__ == "__main__":
    compare_markdown_documents()