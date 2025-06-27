# hello_world.py
# This example demonstrates simple Hello World example to compare documents

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def run():
    
    output_directory = utils.get_output_directory_path()
    output_file_name = join(output_directory, constants.RESULT_WORD)
    
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gc.Comparer(constants.SOURCE_WORD) as comparer:
        # Adding document to compare
        comparer.add(constants.TARGET_WORD)
        # Compare the result
        comparer.compare(output_file_name)

    print(f"\nSource document rendered successfully.\nCheck output in {output_file_name}.")
