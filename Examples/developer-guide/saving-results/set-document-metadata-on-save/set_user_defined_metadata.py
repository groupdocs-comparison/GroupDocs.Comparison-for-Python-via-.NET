from groupdocs.comparison import Comparer
from groupdocs.comparison.options import SaveOptions, MetadataType, FileAuthorMetadata

def set_user_defined_metadata():
    with Comparer("./source.docx") as comparer:
        comparer.add("./target.docx")

        author_metadata = FileAuthorMetadata()
        author_metadata.author = "Tom"
        author_metadata.company = "GroupDocs"
        author_metadata.last_save_by = "Jack"

        save_options = SaveOptions()
        save_options.clone_metadata_type = MetadataType.FILE_AUTHOR
        save_options.file_author_metadata = author_metadata

        comparer.compare("./result.docx", save_options)

if __name__ == "__main__":
    set_user_defined_metadata()