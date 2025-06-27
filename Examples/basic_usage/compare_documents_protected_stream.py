# compare_documents_protected_stream.py
# This example demonstrates comparing two password-protected documents provided as streams.

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def run():
    try:
        # Prepare the output directory and file name
        output_directory = utils.get_output_directory_path()
        output_file_name = join(output_directory, constants.RESULT_WORD)

        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Initialize the comparer with the source file stream and load options
        load_options_source = gc.options.LoadOptions()
        load_options_source.password = "1234"
        with open(constants.SOURCE_WORD_PROTECTED, 'rb') as source_stream:
            comparer = gc.Comparer(source_stream, load_options_source)

            # Add the target file stream and load options for comparison
            load_options_target = gc.options.LoadOptions()
            load_options_target.password="5678"
            with open(constants.TARGET_WORD_PROTECTED, 'rb') as target_stream:
                comparer.add(target_stream, load_options_target)
                comparer.compare(output_file_name)

            # Log the success message with the output file path
            print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")

    except Exception as error:
        # Handle errors
        print(f'An error occurred during the document comparison: {error}')

