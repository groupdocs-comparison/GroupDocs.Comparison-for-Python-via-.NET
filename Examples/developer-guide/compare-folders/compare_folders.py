from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions, FolderComparisonExtension

def compare_folders():
    compare_options = CompareOptions()
    compare_options.directory_compare = True
    compare_options.folder_comparison_extension = FolderComparisonExtension.HTML
    compare_options.show_only_changed = True

    with Comparer("SourceFolder", compare_options) as comparer:
        comparer.add("TargetFolder", compare_options)
        comparer.compare_directory("./result.html", compare_options)
        print("Folders compared successfully. Check output in result.html.")

if __name__ == "__main__":
    compare_folders()