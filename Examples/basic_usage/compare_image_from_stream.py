import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Basic Usage] # CompareImageFromStream : comparing of two images without SummaryPage\n")

    output_directory = c.outputPath
    output_file_name = os.path.join(output_directory, c.RESULT_IMAGE)

    os.makedirs(output_directory, exist_ok=True)

    with open(c.SOURCE_IMAGE, "rb") as source_stream, \
         open(c.TARGET_IMAGE, "rb") as target_stream:

        with Comparer(source_stream) as comparer:
            # If you set the generate_summary_page property to True then the result will be saved in PDF format
            options = CompareOptions()
            options.generate_summary_page = False

            comparer.add(target_stream)
            comparer.compare(output_file_name, options)

    print(f"\nImages compared successfully.\nCheck output in {os.getcwd()}.")


if __name__ == "__main__":
    run()
