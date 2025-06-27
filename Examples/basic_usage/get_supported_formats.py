# get_supported_formats.py
# This example demonstrates retrieving supported file formats.

import groupdocs.comparison as gc

def run():
    try:
        # Retrieve the supported file types
        supported_file_types = gc.result.FileType.get_supported_file_types()

        for file_type in sorted(supported_file_types, key=lambda x: x.extension):
            print(file_type)

        print("\nSupported file types retrieved successfully.")
    except Exception as error:
        print("An error occurred while retrieving supported file types:", error)