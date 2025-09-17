from groupdocs.comparison import Comparer
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Basic Usage] # GetDocumentInfoFromResultDocument : result document object info extraction\n")

    with open(c.SOURCE_WORD, "rb") as source_stream, \
         open(c.TARGET_WORD, "rb") as target_stream:

        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)

            # Access the first target's document info
            info = comparer.targets[0].get_document_info()

            print(f"\nFile type: {info.file_type}")
            print(f"Number of pages: {info.page_count}")
            print(f"Document size: {info.size} bytes")

    print("\nDocument info extracted successfully.")


if __name__ == "__main__":
    run()
