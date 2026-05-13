from groupdocs.comparison import Comparer

def compare_multiple_documents_stream():
    with open("./source.docx", "rb") as src, \
         open("./target1.docx", "rb") as t1, \
         open("./target2.docx", "rb") as t2, \
         open("./target3.docx", "rb") as t3:
        with Comparer(src) as comparer:
            comparer.add(t1)
            comparer.add(t2)
            comparer.add(t3)
            with open("./result.docx", "wb") as out_stream:
                comparer.compare(out_stream)

if __name__ == "__main__":
    compare_multiple_documents_stream()