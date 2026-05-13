import os
import sys
import traceback

# Use UTF-8 for stdout on Windows to avoid encoding errors when printing
# converted Markdown that contains special Unicode characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Set license path (update this path to your license file location)
# os.environ["GROUPDOCS_LIC_PATH"] = "./GroupDocs.Comparison.lic"

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Comparison for Python via .NET Examples!
=================================================================

This script runs a series of examples showcasing how to compare documents and detect differences using GroupDocs.Comparison.
Each example demonstrates different use cases and functionalities such as:

- Comparing documents across 50+ supported formats.
- Detecting added, modified, styled, and deleted content.
- Customizing comparison sensitivity and change styles.
- Accepting or rejecting detected changes.
- Loading password-protected and stream-based documents.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API!

=======================================================
"""
    print(intro_text)

def set_license():
    """Set the GroupDocs license from environment variable or license file."""
    from groupdocs.comparison import License

    # First, check for license path in environment variable
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")

    # Set license if found
    if license_path and os.path.exists(license_path):
        license = License()
        license.set_license(license_path)
        print(f"{GREEN}License set from: {license_path}{RESET}\n")
    else:
        print(f"{YELLOW}No license file found. Running in evaluation mode.{RESET}\n")

def run_example(base_dir, example_path):
    """Run a single example by executing its script in-process."""
    full_path = os.path.join(base_dir, example_path)
    example_dir = os.path.dirname(full_path)

    # Change to the example directory so relative paths work
    saved_cwd = os.getcwd()
    os.chdir(example_dir)
    try:
        code = open(full_path, "r", encoding="utf-8").read()
        exec(compile(code, full_path, "exec"), {"__name__": "__main__", "__file__": full_path})
    finally:
        os.chdir(saved_cwd)

examples = [
    "getting-started/quick-start-guide/quick_start.py",
    "getting-started/quick-start-guide/list_changes.py",
    "licensing/set_license_from_file.py",
    "licensing/set_license_from_stream.py",
    "licensing/set_metered_license.py",
    "developer-guide/comparing-documents/compare-documents/compare_documents.py",
    "developer-guide/comparing-documents/compare-documents/compare_documents_from_stream.py",
    "developer-guide/comparing-documents/compare-documents/compare_documents_to_stream.py",
    "developer-guide/comparing-documents/compare-word-documents/compare_word_documents.py",
    "developer-guide/comparing-documents/compare-pdf-documents/compare_pdf_documents.py",
    "developer-guide/comparing-documents/compare-multiple-documents/compare_multiple_documents.py",
    "developer-guide/comparing-documents/compare-multiple-documents/compare_multiple_documents_stream.py",
    "developer-guide/comparing-documents/compare-multiple-documents/compare_multiple_documents_settings.py",
    "developer-guide/comparing-documents/compare-multiple-documents/compare_multiple_documents_protected.py",
    "developer-guide/comparing-documents/compare-markdown-documents/compare_markdown_documents.py",
    "developer-guide/comparing-documents/compare-json-documents/compare_json_documents.py",
    "developer-guide/comparing-documents/compare-json-documents/compare_json_to_html.py",
    "developer-guide/comparing-documents/compare-json-documents/compare_json_textual.py",
    "developer-guide/comparing-documents/accept-or-reject-detected-changes/accept_or_reject_changes.py",
    "developer-guide/comparing-documents/accept-or-reject-detected-changes/accept_or_reject_changes_stream.py",
    "developer-guide/comparing-documents/accept-or-reject-revisions/accept_or_reject_revisions.py",
    "developer-guide/comparing-documents/accept-or-reject-revisions/accept_or_reject_revisions_stream.py",
    "developer-guide/comparing-documents/accept-or-reject-revisions/accept_all_revisions.py",
    "developer-guide/comparing-documents/adjusting-comparison-sensitivity/adjust_comparison_sensitivity.py",
    "developer-guide/comparing-documents/adjusting-comparison-sensitivity/adjust_comparison_sensitivity_tables.py",
    "developer-guide/comparing-documents/customize-changes-styles/customize_changes_styles.py",
    "developer-guide/comparing-documents/customize-changes-styles/customize_changes_styles_stream.py",
    "developer-guide/comparing-documents/get-list-of-changes/get_list_of_changes.py",
    "developer-guide/comparing-documents/get-list-of-changes/get_list_of_changes_stream.py",
    "developer-guide/comparing-documents/get-changes-coordinates/get_changes_coordinates.py",
    "developer-guide/comparing-documents/get-only-summary-page/get_only_summary_page.py",
    "developer-guide/comparing-documents/get-extended-information-on-the-summary-page/get_extended_summary_information.py",
    "developer-guide/comparing-documents/get-result-document-object/get_result_document_object.py",
    "developer-guide/comparing-documents/get-source-and-target-text-from-files/get_source_and_target_text.py",
    "developer-guide/comparing-documents/get-source-and-target-text-from-files/get_source_and_target_text_stream.py",
    "developer-guide/comparing-documents/compare-bookmarks-in-word/compare_bookmarks_in_word.py",
    "developer-guide/comparing-documents/compare-of-variables-and-document-properties/compare_variables_and_document_properties.py",
    "developer-guide/comparing-documents/disable-image-comparison-in-pdf-documents/disable_image_comparison_in_pdf.py",
    "developer-guide/comparing-documents/set-shape-color-independently-of-font-color/set_shape_color_independently.py",
    "developer-guide/comparing-documents/setting-author-of-changes/set_author_of_changes.py",
    "developer-guide/comparing-documents/how-to-merge-source-code-files/merge_source_code_files.py",
    "developer-guide/comparing-documents/show-gap-lines/show_gap_lines.py",
    "developer-guide/comparing-documents/show-revisions/hide_revisions.py",
    "developer-guide/comparing-documents/specify-file-type-manually/specify_file_type_manually.py",
    "developer-guide/comparing-documents/word-track-changes/include_word_track_changes.py",
    "developer-guide/comparing-documents/word-track-changes/ignore_word_track_changes.py",
    "developer-guide/getting-document-info/get_document_info.py",
    "developer-guide/getting-document-info/get_document_info_from_stream.py",
    "developer-guide/loading-documents/load-file-from-local-disk/load_file_from_local_disk.py",
    "developer-guide/loading-documents/load-file-from-stream/load_file_from_stream.py",
    "developer-guide/loading-documents/load-password-protected-documents/load_password_protected_documents.py",
    "developer-guide/loading-documents/load-custom-fonts/load_custom_fonts.py",
    "developer-guide/compare-folders/compare_folders.py",
    "developer-guide/loading-documents/load-text-from-string/load_text_from_string.py",
    "developer-guide/generate-document-pages-preview/generate_document_pages_preview.py",
    "developer-guide/get-supported-file-formats/get_supported_file_formats.py",
    "developer-guide/logging-and-diagnostics/logging_console.py",
    "developer-guide/saving-results/set-document-metadata-on-save/set_metadata_from_source.py",
    "developer-guide/saving-results/set-document-metadata-on-save/set_metadata_from_target.py",
    "developer-guide/saving-results/set-document-metadata-on-save/set_user_defined_metadata.py",
    "developer-guide/saving-results/set-password-for-resultant-document/set_password_for_resultant_document.py",
    "developer-guide/saving-results/save-comparison-result-in-different-format/save_comparison_result_in_different_format.py",
]

print_intro()
set_license()

base_dir = os.path.dirname(__file__)
passed = 0
failed = 0

for example in examples:
    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        run_example(base_dir, example)
        print(f"{GREEN}Completed {example}{RESET}\n")
        passed += 1
    except Exception as e:
        print(f"{RED}Error in {example}: {type(e).__name__}: {e}{RESET}\n")
        failed += 1

print(f"\n{GREEN}Passed: {passed}{RESET}  {RED}Failed: {failed}{RESET}  Total: {passed + failed}")

sys.exit(1 if failed else 0)
