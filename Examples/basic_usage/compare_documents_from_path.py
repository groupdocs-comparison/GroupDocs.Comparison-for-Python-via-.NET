# compare_documents_from_path.py
# This example demonstrates how to compare documents with the same document file type
# For more details about Document Comparison, please check the documentation
# https://docs.groupdocs.com/comparison

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

        # Initialize the comparer object with the source file path
        with gc.Comparer(constants.SOURCE_WORD) as comparer:
            # Add the target file for comparison and perform the compare operation
            comparer.add(constants.TARGET_WORD)
            comparer.compare(output_file_name)

            # Log the success message with the output file path
            print(f"Compared to {output_file_name}")
    except Exception as error:
        # Handle any errors that might occur during the comparison process
        print(f'An error occurred during the document comparison: {error}')

