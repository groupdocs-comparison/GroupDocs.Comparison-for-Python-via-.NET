from groupdocs.comparison import Comparer

def quick_start():
    # Initialize Comparer with the source document and add the target.
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        # The result file contains the merged comparison highlighting added,
        # deleted, modified, and style changes.
        comparer.compare("./result.docx")

if __name__ == "__main__":
    quick_start()