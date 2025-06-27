# compare_documents_from_stream.py
# This example demonstrates comparing two documents from streams.

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def run():
    try:
        # Prepare the output file path
        output_directory = utils.get_output_directory_path()
        output_file_name = join(output_directory, constants.RESULT_WORD)

        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Initialize the comparer object with the source file stream
        with open(constants.SOURCE_WORD, 'rb') as source_stream:
            comparer = gc.Comparer(source_stream)

            # Add the target file for comparison from a stream and perform the compare operation
            with open(constants.TARGET_WORD, 'rb') as target_stream:
                comparer.add(target_stream)
                comparer.compare(output_file_name)

            # Log the success message with the output file path
            print(f"Compared to {output_file_name}")
    except Exception as error:
        # Handle any errors that might occur during the comparison process
        print(f'An error occurred during the document comparison: {error}')

