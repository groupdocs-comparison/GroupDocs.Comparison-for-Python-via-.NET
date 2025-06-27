# compare_multiple_documents_protected_path.py
# This example demonstrates comparing multiple documents with custom settings loaded by paths and handling protected documents

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def compare_multiple_documents_protected_path(source_path, target_paths, source_password, target_passwords, result_path):
    try:
        output_directory = utils.get_output_directory_path()
        output_file_name = join(output_directory, result_path)
        
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Initialize the comparer with the source file path and load options
        load_options_source = gc.options.LoadOptions()
        load_options_source.password = source_password
        comparer = gc.Comparer(source_path, load_options_source)

        # Add target files and load options
        for target_path, target_password in zip(target_paths, target_passwords):
            load_options_target = gc.options.LoadOptions()
            load_options_target.password = target_password
            comparer.add(target_path, load_options_target)

        # Perform the compare operation and save the result
        comparer.compare(output_file_name)

        print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")
    
    except Exception as error:
        # Handle errors
        print('An error occurred during the document comparison:', error)

def compare_multiple_protected_words_documents():
    compare_multiple_documents_protected_path(
        constants.SOURCE_WORD_PROTECTED, 
        [constants.TARGET_WORD_PROTECTED, constants.TARGET2_WORD_PROTECTED, constants.TARGET3_WORD_PROTECTED], 
        "1234", 
        ["5678", "5678", "5678"], 
        constants.RESULT_WORD
    )
