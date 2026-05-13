from groupdocs.comparison import Comparer

def load_file_from_stream():
    with open("./source.docx", "rb") as source_stream, \
         open("./target.docx", "rb") as target_stream:
        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare("./result.docx")
            print("Documents compared successfully. Check output in result.docx.")

if __name__ == "__main__":
    load_file_from_stream()