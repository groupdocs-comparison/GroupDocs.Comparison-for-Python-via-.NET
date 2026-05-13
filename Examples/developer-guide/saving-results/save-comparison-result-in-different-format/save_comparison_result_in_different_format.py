from groupdocs.comparison import Comparer

def save_comparison_result_in_different_format():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        # Output is inferred from the file extension — .pdf in this case.
        comparer.compare("./result.pdf")

if __name__ == "__main__":
    save_comparison_result_in_different_format()