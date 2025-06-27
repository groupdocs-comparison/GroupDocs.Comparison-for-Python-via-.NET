# get_document_info_stream.py
# This example demonstrates document information extraction.

import groupdocs.comparison as gc
import constants

def run():
    with open(constants.SOURCE_WORD, 'rb') as source_stream:
        comparer = gc.Comparer(source_stream)

        info = comparer.source.get_document_info()
        
        print(f"\nFile type: {info.file_type.file_format}")
        print(f"Number of pages: {info.page_count}")
        print(f"Document size: {info.size} bytes")
        
        print("\nDocument info extracted successfully.")
