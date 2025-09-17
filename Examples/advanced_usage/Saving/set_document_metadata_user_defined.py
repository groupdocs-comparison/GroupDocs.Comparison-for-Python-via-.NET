import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import SaveOptions, MetadataType, FileAuthorMetadata
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # SetDocumentMetadataUserDefined : using option for select user metadata\n")

    output_directory = c.outputPath
    output_file_name = os.path.join(output_directory, c.RESULT_WORD)

    os.makedirs(output_directory, exist_ok=True)

    with Comparer(c.SOURCE_WORD) as comparer:
        comparer.add(c.TARGET_WORD)

        save_options = SaveOptions()
        save_options.clone_metadata_type = MetadataType.FILE_AUTHOR
        save_options.file_author_metadata = FileAuthorMetadata(
            author="Tom",
            company="GroupDocs",
            last_save_by="Jack"
        )

        comparer.compare(output_file_name, save_options)

    print(f"\nDocuments compared successfully.\nCheck output in {output_directory}.")


if __name__ == "__main__":
    run()
