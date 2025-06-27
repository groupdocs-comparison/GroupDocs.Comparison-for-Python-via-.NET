# compare_multiple_documents_protected_stream.py
# This example demonstrates comparing multiple documents with custom settings loaded by streams and handling protected documents

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def compare_multiple_documents_protected_stream(source_path, target_paths, source_password, target_passwords, result_path):
    try:
        output_directory = utils.get_output_directory_path()
        output_file_name = join(output_directory, result_path)
        
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Initialize the comparer with the source stream and load options
        with open(source_path, 'rb') as source_stream:
            load_options_source = gc.options.LoadOptions()
            load_options_source.password = source_password
            comparer = gc.Comparer(source_stream, load_options_source)

            # Add target streams and load options
            target_streams = []
            for target_path, target_password in zip(target_paths, target_passwords):
                target_stream = open(target_path, 'rb')
                target_streams.append(target_stream)
                load_options_target = gc.options.LoadOptions()
                load_options_target.password = target_password
                comparer.add(target_stream, load_options_target)

            # Perform the compare operation and save the result
            comparer.compare(output_file_name)

            # Close target streams after comparison
            for target_stream in target_streams:
                target_stream.close()

        print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")
    
    except Exception as error:
        # Handle errors
        print('An error occurred during the document comparison:', error)

def compare_multiple_protected_words_documents():
    compare_multiple_documents_protected_stream(
        constants.SOURCE_WORD_PROTECTED, 
        [constants.TARGET_WORD_PROTECTED, constants.TARGET2_WORD_PROTECTED, constants.TARGET3_WORD_PROTECTED], 
        "1234", 
        ["5678", "5678", "5678"], 
        constants.RESULT_WORD
    )
