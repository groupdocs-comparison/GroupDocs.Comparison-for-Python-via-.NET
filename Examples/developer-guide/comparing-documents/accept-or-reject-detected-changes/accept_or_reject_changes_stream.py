from groupdocs.comparison import Comparer
from groupdocs.comparison.options import ApplyChangeOptions
from groupdocs.comparison.result import ComparisonAction

def accept_or_reject_changes_stream():
    with open("./source.docx", "rb") as source_stream, \
         open("./target.docx", "rb") as target_stream:
        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare()
            changes = comparer.get_changes()
            if changes:
                changes[0].comparison_action = ComparisonAction.REJECT
            with open("./result.docx", "wb") as out_stream:
                comparer.apply_changes(out_stream, ApplyChangeOptions(changes=changes))

if __name__ == "__main__":
    accept_or_reject_changes_stream()