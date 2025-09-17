import os
from groupdocs.comparison import Comparer
import constants as c  # your constants.py file

def run():
    print("\n" + "-" * 116)
    print("[Example Basic Usage] # CompareCellsFromPath : comparing of two cells files\n")

    output_directory = c.outputPath
    output_file_name = os.path.join(output_directory, c.RESULT_CELLS)

    os.makedirs(output_directory, exist_ok=True)

    with Comparer(c.SOURCE_CELLS) as comparer:
        comparer.add(c.TARGET_CELLS)
        comparer.compare(output_file_name)

    print(f"\nDocuments compared successfully.\nCheck output in {output_directory}.")


if __name__ == "__main__":
    run()
