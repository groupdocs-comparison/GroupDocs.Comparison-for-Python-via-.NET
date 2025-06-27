# compare_folders.py
# This example demonstrates how to compare folders and save the result in a specified format.

import groupdocs.comparison as gc
import os
from os.path import join
import constants
import utils

def compare_folders(output_format):
    try:
        output_directory = utils.get_output_directory_path()
        output_file_name = join(output_directory, constants.RESULT_FOLDER + ('.html' if output_format == 'HTML' else '.txt'))

        # Set compare options for directory comparison
        compare_options = gc.options.CompareOptions()
        compare_options.directory_compare = True
        compare_options.folder_comparison_extension = (
            gc.options.FolderComparisonExtension.HTML
            if output_format == 'HTML'
            else gc.options.FolderComparisonExtension.TXT
        )

        # Create a new comparer with the source folder path and comparison options
        comparer = gc.Comparer(constants.SOURCE_FOLDER, compare_options)

        # Add the target folder for comparison
        comparer.add(constants.TARGET_FOLDER, compare_options)

        # Perform the comparison and save the result
        comparer.compare_directory(output_file_name, compare_options)

        print(f"\nFolders compared successfully.\nCheck output in {output_file_name}.")

    except Exception as error:
        # Handle errors
        print('An error occurred during the folder comparison:', error)

def compare_folder_save_as_txt():
    compare_folders('TXT')

def compare_folder_save_as_html():
    compare_folders('HTML')
