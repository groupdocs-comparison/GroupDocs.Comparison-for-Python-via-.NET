# compare_multiple_pdf_documents.py
# This example demonstrates comparing multiple PDF documents.
# For more details about comparing PDF documents, please check the relevant documentation.

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def run():
    try:
        # Initialize comparer with the source PDF document
        comparer = gc.Comparer(constants.SOURCE_PDF)
        
        # Prepare the output file path
        output_directory = utils.get_output_directory_path()
        output_file_name = join(output_directory, constants.RESULT_PDF)
        
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Add multiple target PDF documents for comparison
        for target_file_path in [constants.TARGET_PDF, constants.TARGET2_PDF, constants.TARGET3_PDF]:
            comparer.add(target_file_path)
        
        # Compare the PDF documents and save the result
        comparer.compare(output_file_name)
        
        # Log the success message with the output file path
        print(f"PDF documents compared successfully. Check output in {output_file_name}")
    
    except Exception as error:
        # Error handling
        print(f'An error occurred during the PDF documents comparison: {error}')

