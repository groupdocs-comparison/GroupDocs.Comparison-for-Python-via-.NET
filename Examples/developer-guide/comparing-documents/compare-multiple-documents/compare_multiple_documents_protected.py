from groupdocs.comparison import Comparer
from groupdocs.comparison.options import LoadOptions

def compare_multiple_documents_protected():
    source_load = LoadOptions()
    source_load.password = "1234"

    with Comparer("./source_protected.docx", source_load) as comparer:
        for target, password in (
            ("./target_protected.docx", "5678"),
            ("./target2_protected.docx", "5678"),
            ("./target3_protected.docx", "5678"),
        ):
            load_opts = LoadOptions()
            load_opts.password = password
            comparer.add(target, load_opts)

        comparer.compare("./result.docx")

if __name__ == "__main__":
    compare_multiple_documents_protected()