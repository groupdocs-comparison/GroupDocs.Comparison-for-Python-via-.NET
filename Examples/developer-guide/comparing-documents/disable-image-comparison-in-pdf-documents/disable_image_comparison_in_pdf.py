from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions, ImagesInheritance

def disable_image_comparison_in_pdf():
    with Comparer("./source.pdf") as comparer:
        comparer.add("./target.pdf")
        options = CompareOptions()
        options.compare_images_pdf = False
        options.images_inheritance_mode = ImagesInheritance.TARGET
        comparer.compare("./result.pdf", options)

if __name__ == "__main__":
    disable_image_comparison_in_pdf()