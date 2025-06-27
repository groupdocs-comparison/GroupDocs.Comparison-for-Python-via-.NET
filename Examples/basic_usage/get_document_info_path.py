# get_document_info_path.py
# This example demonstrates document information extraction.
# For more details about extracting document information, please check the relevant documentation.

import groupdocs.comparison as gc
import constants

def run():
    comparer = gc.Comparer(constants.SOURCE_WORD)

    info = comparer.source.get_document_info()

    print(info)
    
    print(f"\nFile type: {info.file_type.file_format}")
    print(f"Number of pages: {info.page_count}")
    print(f"Document size: {info.size} bytes")
    
    print("\nDocument info extracted successfully.")
