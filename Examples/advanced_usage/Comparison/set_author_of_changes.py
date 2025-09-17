import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # SetAuthorOfChanges : how to set author of changes\n")

    output_directory = c.outputPath
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, c.RESULT_WITH_NEW_AUTHOR_WORD)

    with Comparer(c.SOURCE_WORD) as comparer:
        compare_options = CompareOptions()
        compare_options.show_revisions = True
        compare_options.word_track_changes = True
        compare_options.revision_author_name = "New author"

        comparer.add(c.TARGET_WORD)
        comparer.compare(output_file, compare_options)

    print(f"\nChanges updated successfully.\nCheck output in {os.getcwd()}")


if __name__ == "__main__":
    run()
