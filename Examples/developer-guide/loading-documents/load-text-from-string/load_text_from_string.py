from groupdocs.comparison import Comparer
from groupdocs.comparison.options import LoadOptions

def load_text_from_string():
    load_options = LoadOptions()
    load_options.load_text = True

    with Comparer("source text", load_options) as comparer:
        comparer.add("target text", load_options)
        comparer.compare("./result.docx")
        print("Result string:")
        print(comparer.get_result_string())

if __name__ == "__main__":
    load_text_from_string()