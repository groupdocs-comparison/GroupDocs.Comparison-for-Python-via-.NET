from groupdocs.comparison import Comparer
from groupdocs.comparison.options import SaveOptions, MetadataType

def set_metadata_from_target():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")
        save_options = SaveOptions()
        save_options.clone_metadata_type = MetadataType.TARGET
        comparer.compare("./result.docx", save_options)

if __name__ == "__main__":
    set_metadata_from_target()