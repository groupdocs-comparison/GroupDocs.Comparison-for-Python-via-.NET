# compare_multiple_documents_path.py
# This example demonstrates comparing multiple documents with custom settings loaded by file path

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def compare_multiple_documents(source_path, target_paths, result_path):
    try:
        output_directory = utils.get_output_directory_path()
        output_file_name = join(output_directory, result_path)
        
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Initialize the comparer with the source file
        comparer = gc.Comparer(source_path)
        
        # Add target files
        for target_path in target_paths:
            comparer.add(target_path)

        # Set comparison options and save options
        save_options = gc.options.SaveOptions()
        compare_options = gc.options.CompareOptions()

        # Perform the compare operation and save the result
        comparer.compare(output_file_name, save_options, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")
    
    except Exception as error:
        # Handle errors
        print('An error occurred during the document comparison:', error)

def compare_multiple_words_documents():
    compare_multiple_documents(constants.SOURCE_WORD, [constants.TARGET_WORD, constants.TARGET2_WORD, constants.TARGET3_WORD], constants.RESULT_WORD)

def compare_multiple_txt_documents():
    compare_multiple_documents(constants.SOURCE_TXT, [constants.TARGET_TXT, constants.TARGET2_TXT, constants.TARGET3_TXT], constants.RESULT_TXT)

def compare_multiple_pdf_documents():
    compare_multiple_documents(constants.SOURCE_PDF, [constants.TARGET_PDF, constants.TARGET2_PDF, constants.TARGET3_PDF], constants.RESULT_PDF)

# # Execute the functions for specific document types
# compare_multiple_words_documents()
# compare_multiple_txt_documents()
# compare_multiple_pdf_documents()
