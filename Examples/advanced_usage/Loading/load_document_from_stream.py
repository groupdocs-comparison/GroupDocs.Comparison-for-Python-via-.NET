# load_document_from_stream.py
# This example demonstrates comparing two documents loaded by file stream

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def run():
    # Prepare the output directory and file name
    output_directory = utils.get_output_directory_path()
    output_file_name = join(output_directory, constants.RESULT_WORD)
    
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Initialize comparer with the source document using a file stream
    with open(constants.SOURCE_WORD, 'rb') as source_stream:
        with gc.Comparer(source_stream) as comparer:
            # Add the target document for comparison using a file stream
            with open(constants.TARGET_WORD, 'rb') as target_stream:
                comparer.add(target_stream)
            
                # Compare the documents and save the result
                comparer.compare(output_file_name)
    
    # Log the success message with the output file path
    print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")