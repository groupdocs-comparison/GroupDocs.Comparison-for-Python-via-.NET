from groupdocs.comparison import Comparer

def get_source_and_target_text():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        comparer.compare("./result.docx")
        for change in comparer.get_changes():
            print(f"Source text: {change.source_text}")
            print(f"Target text: {change.target_text}\n")

if __name__ == "__main__":
    get_source_and_target_text()