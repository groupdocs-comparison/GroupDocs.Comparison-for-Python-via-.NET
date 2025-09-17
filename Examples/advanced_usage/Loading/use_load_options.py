import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import LoadOptions
import constants as c  # your constants.py

def load_custom_fonts():
    print("\n" + "-" * 116)	
    print("[Example Advanced Usage] # UseLoadOptions : how to load custom font for comparison\n")

    # Need to set the directory of the file with the font
    font_directories = [c.CUSTOM_FONT]

    # Instantiate the LoadOptions object and pass in a list of directories with custom fonts
    load_options = LoadOptions()
    load_options.font_directories = font_directories

    output_directory = c.outputPath
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, c.RESULT_WORD_FONT)

    with open(c.SOURCE_WORD_FONT, "rb") as source_stream, \
         open(c.TARGET_WORD_FONT, "rb") as target_stream, \
         open(output_file, "wb") as result_stream:

        with Comparer(source_stream, load_options) as comparer:
            comparer.add(target_stream)
            comparer.compare(result_stream)

    print(f"\nDocuments compared successfully.\nCheck output in {os.getcwd()}.")


if __name__ == "__main__":
    load_custom_fonts()
