from groupdocs.comparison import Comparer
from groupdocs.comparison.options import LoadOptions

def load_password_protected_documents():
    source_load = LoadOptions()
    source_load.password = "1234"

    target_load = LoadOptions()
    target_load.password = "5678"

    with Comparer("./source_protected.docx", source_load) as comparer:
        comparer.add("./target_protected.docx", target_load)
        comparer.compare("./result.docx")

if __name__ == "__main__":
    load_password_protected_documents()