import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.result import ChangeInfo, ComparisonAction
from groupdocs.comparison.options import ApplyChangeOptions
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # AcceptRejectDetectedChangesPath : How to update changes from path\n")

    output_directory = c.outputPath
    os.makedirs(output_directory, exist_ok=True)

    output_file_accepted = os.path.join(output_directory, c.RESULT_WITH_ACCEPTED_CHANGE_WORD)
    output_file_rejected = os.path.join(output_directory, c.RESULT_WITH_REJECTED_CHANGE_WORD)

    with Comparer(c.SOURCE_WORD) as comparer:
        comparer.add(c.TARGET_WORD)
        comparer.compare()

        changes = comparer.get_changes()

        # Example: Reject the first detected change
        changes[0].comparison_action = ComparisonAction.REJECT
        comparer.apply_changes(output_file_rejected,
                               ApplyChangeOptions(changes=changes, save_original_state=True))

        # Example: Accept the first detected change
        changes = comparer.get_changes()
        changes[0].comparison_action = ComparisonAction.ACCEPT
        comparer.apply_changes(output_file_accepted, ApplyChangeOptions(changes=changes))

    print(f"\nChanges updated successfully.\nCheck output in {output_directory}.")


if __name__ == "__main__":
    run()
