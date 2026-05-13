from groupdocs.comparison import Comparer
from groupdocs.comparison.options import ApplyChangeOptions
from groupdocs.comparison.result import ComparisonAction

def accept_or_reject_changes():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        comparer.compare()
        changes = comparer.get_changes()

        # Reject the first change; accept everything else
        if changes:
            changes[0].comparison_action = ComparisonAction.REJECT

        comparer.apply_changes("./result.docx", ApplyChangeOptions(changes=changes))

if __name__ == "__main__":
    accept_or_reject_changes()