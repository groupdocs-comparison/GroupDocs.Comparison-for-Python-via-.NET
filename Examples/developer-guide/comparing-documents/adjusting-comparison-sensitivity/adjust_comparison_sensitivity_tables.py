from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions

def adjust_comparison_sensitivity_tables():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        options = CompareOptions()
        options.sensitivity_of_comparison = 100
        options.sensitivity_of_comparison_for_tables = 75
        comparer.compare("./result.docx", options)

if __name__ == "__main__":
    adjust_comparison_sensitivity_tables()