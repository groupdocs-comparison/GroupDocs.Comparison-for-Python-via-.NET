# compare_multiple_documents_stream.py
# This example demonstrates comparing multiple documents loaded by file stream

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

        # Initialize the comparer with the source file stream
        with open(constants.SOURCE_WORD, 'rb') as source_stream:
            comparer = gc.Comparer(source_stream)
        
            # Add the target file streams
            with open(constants.TARGET_WORD, 'rb') as target_stream1, \
                 open(constants.TARGET2_WORD, 'rb') as target_stream2, \
                 open(constants.TARGET3_WORD, 'rb') as target_stream3:
                 
                comparer.add(target_stream1)
                comparer.add(target_stream2)
                comparer.add(target_stream3)

                # Perform the compare operation and save the result
                comparer.compare(output_file_name)

        print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")
    
    except Exception as error:
        # Handle errors
        print('An error occurred during the document comparison:', error)
