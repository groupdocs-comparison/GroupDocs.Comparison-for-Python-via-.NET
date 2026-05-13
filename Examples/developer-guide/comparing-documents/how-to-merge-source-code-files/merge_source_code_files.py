from groupdocs.comparison import Comparer
from groupdocs.comparison.options import ApplyChangeOptions
from groupdocs.comparison.result import ComparisonAction

def merge_source_code_files():
    with Comparer("./source.cs") as comparer:
        comparer.add("./target.cs")
        comparer.compare("./result.cs")
        changes = comparer.get_changes()

        # Accept the first 10 changes; reject the rest
        for i, change in enumerate(changes):
            change.comparison_action = ComparisonAction.ACCEPT if i < 10 else ComparisonAction.REJECT

        with open("./result.cs", "wb") as result_file:
            comparer.apply_changes(result_file, ApplyChangeOptions(changes=changes))

if __name__ == "__main__":
    merge_source_code_files()