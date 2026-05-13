from groupdocs.comparison import Comparer

def load_file_from_local_disk():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        comparer.compare("./result.docx")
        print("Documents compared successfully. Check output in result.docx.")

if __name__ == "__main__":
    load_file_from_local_disk()