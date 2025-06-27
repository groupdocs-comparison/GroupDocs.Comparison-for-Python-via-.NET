# compare_multiple_documents_settings_path.py
# This example demonstrates comparing multiple documents with custom settings loaded by file path

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils
from groupdocs.pydrawing import Color

def run():
    try:
        # Prepare the output directory and file name
        output_directory = utils.get_output_directory_path()
        output_file_name = join(output_directory, constants.RESULT_WORD)
        
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Initialize the comparer with the source file
        comparer = gc.Comparer(constants.SOURCE_WORD)
        
        # Add the target files
        comparer.add(constants.TARGET_WORD)
        comparer.add(constants.TARGET2_WORD)
        comparer.add(constants.TARGET3_WORD)

        # Set comparison options and style settings
        compare_options = gc.options.CompareOptions()
        style_settings = gc.options.StyleSettings()
        style_settings.font_color = Color.yellow
        compare_options.inserted_item_style = style_settings

        # Perform the compare operation and save the result
        comparer.compare(output_file_name, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")
    
    except Exception as error:
        # Handle errors
        print('An error occurred during the document comparison:', error)
