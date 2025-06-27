# set_password_for_resultant_document.py
# This example demonstrates how to protect the resultant document by password

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
        
        # Initialize comparer with the source document
        with gc.Comparer(constants.SOURCE_WORD) as comparer:
            # Add the target document for comparison
            comparer.add(constants.TARGET_WORD)
            
            # Set comparison options
            compare_options = gc.options.CompareOptions()
            compare_options.password_save_option = gc.options.PasswordSaveOption.USER
            
            # Set save options
            save_options = gc.options.SaveOptions()
            save_options.password = "3333"
            
            # Compare the documents and save the result
            comparer.compare(output_file_name, save_options, compare_options)
        
        # Log the success message with the output file path
        print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")
    
    except Exception as error:
        # Error handling
        print(f'An error occurred during the document comparison: {error}')