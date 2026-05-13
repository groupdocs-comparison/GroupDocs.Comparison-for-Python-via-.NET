from groupdocs.comparison import Comparer

def get_source_and_target_text_stream():
    with open("./source.docx", "rb") as source_stream, \
         open("./target.docx", "rb") as target_stream:
        with Comparer(source_stream) as comparer:
            comparer.add(target_stream)
            comparer.compare("./result.docx")
            for change in comparer.get_changes():
                print(f"Source text: {change.source_text}")
                print(f"Target text: {change.target_text}\n")

if __name__ == "__main__":
    get_source_and_target_text_stream()