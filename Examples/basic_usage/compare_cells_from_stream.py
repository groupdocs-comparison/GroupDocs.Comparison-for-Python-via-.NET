import os
from groupdocs.comparison import Comparer
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Basic Usage] # CompareCellsFromStream : comparing of two cells files\n")

    output_directory = c.outputPath
    output_file_name = os.path.join(output_directory, c.RESULT_CELLS)

    os.makedirs(output_directory, exist_ok=True)

    with open(c.SOURCE_CELLS, "rb") as source_stream, \
         open(c.TARGET_CELLS, "rb") as target_stream, \
         open(output_file_name, "wb") as result_stream:

        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare(result_stream)

    print(f"\nDocuments compared successfully.\nCheck output in {output_directory}.")


if __name__ == "__main__":
    run()
