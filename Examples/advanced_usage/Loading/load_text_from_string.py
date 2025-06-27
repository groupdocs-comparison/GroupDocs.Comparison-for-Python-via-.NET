# load_text_from_string.py
# This example demonstrates comparing two texts loaded by string variables

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def run():
    # Prepare the output directory and file name
    output_directory = utils.get_output_directory_path()
    output_file_name = join(output_directory, constants.RESULT_TXT)
    
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Initialize LoadOptions and set to load text
    load_options = gc.options.LoadOptions()
    load_options.load_text = True

    # Initialize comparer with the source text using LoadOptions
    with gc.Comparer("source text", load_options) as comparer:
        # Add the target text for comparison using LoadOptions
        comparer.add("target text", load_options)
        
        # Compare the texts and save the result
        comparer.compare(output_file_name)

        # Print the result string
        print("Result string: \n" + comparer.get_result_string())
    
    # Log the success message with the output file path
    print(f"\nDocuments compared successfully.\nCheck output in {output_file_name}.")