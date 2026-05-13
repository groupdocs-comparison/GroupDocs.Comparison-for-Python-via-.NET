from groupdocs.comparison import Comparer

def compare_json_documents():
    with Comparer("./source.json") as comparer:
        comparer.add("./target.json")
        comparer.compare("./result_json.json")

if __name__ == "__main__":
    compare_json_documents()