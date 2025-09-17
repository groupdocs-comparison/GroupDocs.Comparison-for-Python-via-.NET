import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Basic Usage] # CompareImageFromPath : comparing of two images without SummaryPage\n")

    output_directory = c.outputPath
    output_file_name = os.path.join(output_directory, c.RESULT_IMAGE)

    os.makedirs(output_directory, exist_ok=True)

    with Comparer(c.SOURCE_IMAGE) as comparer:
        # If you set the GenerateSummaryPage property to True then the result will be saved in PDF format
        options = CompareOptions()
        options.generate_summary_page = False

        comparer.add(c.TARGET_IMAGE)
        comparer.compare(output_file_name, options)

    print(f"\nImages compared successfully.\nCheck output in {os.getcwd()}.")


if __name__ == "__main__":
    run()
