import os
from groupdocs.comparison import Comparer
from groupdocs.comparison.options import CompareOptions, StyleSettings, PaperSize, SaveOptions
import constants as c  # your constants.py

class UseCompareOptions:

    @staticmethod
    def ignore_header_footer():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # IgnoreHeaderFooter : how to ignore Header/Footer\n")

        output_dir = os.path.join(c.outputPath, "IgnoreHeaderFooter")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_WITH_FOOTER) as comparer:
            compare_options = CompareOptions()
            compare_options.header_footers_comparison = False
            comparer.add(c.TARGET_WITH_FOOTER)
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def set_output_paper_size():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # SetOutputPaperSize : how to set output paper size\n")

        output_dir = os.path.join(c.outputPath, "SetOutputPaperSize")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            compare_options.paper_size = PaperSize.A6
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def adjust_comparison_sensitivity():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # AdjustComparisonSensitivity : comparing of two documents using sensitivity option\n")

        output_dir = os.path.join(c.outputPath, "AdjustComparisonSensitivity")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            compare_options.sensitivity_of_comparison = 100
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def customize_changes_styles_stream():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # CustomizeChangesStylesStream : how to customize change styles from stream\n")

        output_dir = os.path.join(c.outputPath, "CustomizeChangesStylesStream")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            # Inserted item style
            compare_options.inserted_item_style = StyleSettings(
                highlight_color="Red", font_color="Green",
                is_underline=True, is_bold=True, is_strikethrough=True, is_italic=True
            )
            # Deleted item style
            compare_options.deleted_item_style = StyleSettings(
                highlight_color="Azure", font_color="Brown",
                is_underline=True, is_bold=True, is_strikethrough=True, is_italic=True
            )
            # Changed item style
            compare_options.changed_item_style = StyleSettings(
                highlight_color="Crimson", font_color="Firebrick",
                is_underline=True, is_bold=True, is_strikethrough=True, is_italic=True
            )

            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def get_only_summary_page():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # GetOnlySummaryPage : how to get only summary page\n")

        output_dir = os.path.join(c.outputPath, "GetOnlySummaryPage")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            compare_options.generate_summary_page = True
            compare_options.show_only_summary_page = True
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def get_extended_summary_page():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # GetExtendedSummaryPage : how to get extended comparison info\n")

        output_dir = os.path.join(c.outputPath, "GetExtendedSummaryPage")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            compare_options.generate_summary_page = True
            compare_options.extended_summary_page = True
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def compare_document_properties():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # CompareDocumentProperties : how to activate compare properties\n")

        output_dir = os.path.join(c.outputPath, "CompareDocumentProperties")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            compare_options.compare_variable_property = True
            compare_options.compare_document_property = True
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def compare_bookmarks():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # CompareBookmarks : how to activate compare bookmarks\n")

        output_dir = os.path.join(c.outputPath, "CompareBookmarks")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            compare_options.compare_bookmarks = True
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def disable_show_revisions():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # DisableShowRevisions : how to disable show revisions\n")

        output_dir = os.path.join(c.outputPath, "DisableShowRevisions")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            compare_options.show_revisions = False
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def leave_gaps():
        print("\n" + "-" * 116)
        print("[Example Advanced Usage] # LeaveGaps : replace changed content with empty lines\n")

        output_dir = os.path.join(c.outputPath, "LeaveGaps")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            compare_options.show_inserted_content = False
            compare_options.show_deleted_content = False
            compare_options.leave_gaps = True
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")

    @staticmethod
    def word_track_changes():
        print("\n" + "-" * 116)
        print('[Example Advanced Usage] # WordTrackChanges : how to use Word "Track Changes"\n')

        output_dir = os.path.join(c.outputPath, "WordTrackChanges")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, c.RESULT_WORD)

        with Comparer(c.SOURCE_COMPARE_OPTIONS) as comparer:
            comparer.add(c.TARGET_COMPARE_OPTIONS)
            compare_options = CompareOptions()
            compare_options.word_track_changes = True
            comparer.compare(output_file, compare_options)

        print(f"\nDocuments compared successfully.\nCheck output in {output_dir}")
