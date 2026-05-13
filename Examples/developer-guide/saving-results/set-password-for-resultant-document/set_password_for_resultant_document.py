from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions, SaveOptions, PasswordSaveOption

def set_password_for_resultant_document():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")

        compare_options = CompareOptions()
        compare_options.password_save_option = PasswordSaveOption.USER

        save_options = SaveOptions()
        save_options.password = "3333"

        comparer.compare("./result.docx", save_options, compare_options)

if __name__ == "__main__":
    set_password_for_resultant_document()