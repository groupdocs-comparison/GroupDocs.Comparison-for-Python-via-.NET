from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def compare_variables_and_document_properties():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        options = CompareOptions()
        options.compare_variable_property = True
        options.compare_document_property = True
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    compare_variables_and_document_properties()