import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions, StyleSettings
from System.Drawing import Color
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # CompareDocumentsSettingsStream : Using some of compare settings\n")

    output_directory = c.outputPath
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, c.RESULT_WORD)

    with open(c.SOURCE_WORD, "rb") as source_stream, \
         open(c.TARGET_WORD, "rb") as target_stream:

        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)

            compare_options = CompareOptions()
            compare_options.inserted_item_style = StyleSettings()
            compare_options.inserted_item_style.highlight_color = Color.Red
            compare_options.inserted_item_style.font_color = Color.Green
            compare_options.inserted_item_style.is_underline = True

            with open(output_file, "wb") as result_stream:
                comparer.compare(result_stream, compare_options)

    print(f"\nDocuments compared successfully.\nCheck output in {os.getcwd()}")


if __name__ == "__main__":
    run()
