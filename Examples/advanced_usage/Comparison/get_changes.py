import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.result import ChangeInfo
from groupdocs.comparison.options import CompareOptions
import constants as c  # your constants.py

def get_changes_coordinates():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # GetChangesCoordinates : how to get changes coordinates\n")

    output_directory = c.outputPath
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, c.RESULT_WORD)

    with open(c.SOURCE_WORD, "rb") as source_stream, \
         open(c.TARGET_WORD, "rb") as target_stream, \
         open(output_file, "wb") as result_stream:

        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            compare_options = CompareOptions()
            compare_options.calculate_coordinates = True
            comparer.compare(result_stream, compare_options)

            changes = comparer.get_changes()
            for change in changes:
                print(f"Change Type: {change.type}, X: {change.box.X}, Y: {change.box.Y}, Text: {change.text}")

    print(f"\nDocuments compared successfully.\nCheck output in {output_directory}.")


def get_list_of_changes_path():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # GetListOfChangesPath : how to get changes from path\n")

    with Comparer(c.SOURCE_WORD) as comparer:
        comparer.add(c.TARGET_WORD)
        comparer.compare()
        changes = comparer.get_changes()

    print("\nChanges received successfully.")


def get_list_of_changes_stream():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # GetListOfChangesStream : how to get changes from stream\n")

    with open(c.SOURCE_WORD, "rb") as source_stream, \
         open(c.TARGET_WORD, "rb") as target_stream:

        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare()
            changes = comparer.get_changes()

    print("\nChanges received successfully.")


def get_source_and_target_texts():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # GetSourceAndTargetTexts : how to get source and target texts\n")

    with open(c.SOURCE_WORD, "rb") as source_stream, \
         open(c.TARGET_WORD, "rb") as target_stream:

        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare()

            changes = comparer.get_changes()
            for change in changes:
                print("\nSource text:", change.source_text)
                print("Target text:", change.target_text)

    print("\nGet Source and Target Texts received successfully.")


if __name__ == "__main__":
    get_changes_coordinates()
    get_list_of_changes_path()
    get_list_of_changes_stream()
    get_source_and_target_texts()
