import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.result import ChangeInfo, ComparisonAction
from groupdocs.comparison.options import ApplyChangeOptions
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # AcceptRejectDetectedChangesStream : How to update changes from stream\n")

    output_directory = c.outputPath
    os.makedirs(output_directory, exist_ok=True)

    output_file_accepted = os.path.join(output_directory, c.RESULT_WITH_ACCEPTED_CHANGE_WORD)
    output_file_rejected = os.path.join(output_directory, c.RESULT_WITH_REJECTED_CHANGE_WORD)

    with open(c.SOURCE_WORD, "rb") as source_stream, \
         open(c.TARGET_WORD, "rb") as target_stream:

        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare()

            changes = comparer.get_changes()

            # Reject the first detected change
            changes[0].comparison_action = ComparisonAction.REJECT
            with open(output_file_rejected, "wb") as result_stream:
                comparer.apply_changes(result_stream,
                                       ApplyChangeOptions(changes=changes, save_original_state=True))

            # Accept the first detected change
            changes = comparer.get_changes()
            changes[0].comparison_action = ComparisonAction.ACCEPT
            with open(output_file_accepted, "wb") as result_stream:
                comparer.apply_changes(result_stream, ApplyChangeOptions(changes=changes))

    print(f"\nChanges updated successfully.\nCheck output in {output_directory}.")


if __name__ == "__main__":
    run()
