from groupdocs.comparison.result import FileType

def get_supported_file_formats():
    supported_file_types = FileType.get_supported_file_types()
    for file_type in sorted(supported_file_types, key=lambda x: x.extension):
        print(file_type)
    print("\nSupported file types retrieved successfully.")

if __name__ == "__main__":
    get_supported_file_formats()