# set_document_metadata_target.py
# This example demonstrates using options to select metadata

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
        
        # Initialize comparer with the target document
        with gc.Comparer(constants.TARGET_WORD) as comparer:
            # Add the target document for comparison
            comparer.add(constants.TARGET_WORD)
            
            # Set comparison options
            save_options = gc.options.SaveOptions()
            save_options.clone_metadata_type = gc.options.MetadataType.TARGET
            
            # Compare the documents and save the result
            comparer.compare(output_file_name, save_options)
        
        # Log the success message with the output file path
        print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")
    
    except Exception as error:
        # Error handling
        print(f'An error occurred during the document comparison: {error}')
