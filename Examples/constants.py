# constants.py
# This module defines paths to test files.

import os
from os.path import join
import platform
import utils

def get_sample_file_path(file_path):
    if platform.system() == 'Windows':
        return join(utils.samples_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, utils.samples_path, file_path)


outputPath = "Results/Output"

SOURCE_WORD = get_sample_file_path("source.docx")
SOURCE_WORD_FONT = get_sample_file_path("source_font.docx")
TARGET_WORD = get_sample_file_path("target.docx")
TARGET_WORD_FONT = get_sample_file_path("target_font.docx")
TARGET2_WORD = get_sample_file_path("target2.docx")
TARGET3_WORD = get_sample_file_path("target3.docx")
SOURCE_WORD_PROTECTED = get_sample_file_path("source_protected.docx")
TARGET_WORD_PROTECTED = get_sample_file_path("target_protected.docx")
TARGET2_WORD_PROTECTED = get_sample_file_path("target2_protected.docx")
TARGET3_WORD_PROTECTED = get_sample_file_path("target3_protected.docx")

SOURCE_TXT = get_sample_file_path("source.txt")
TARGET_TXT = get_sample_file_path("target.txt")
TARGET2_TXT = get_sample_file_path("target2.txt")
TARGET3_TXT = get_sample_file_path("target3.txt")

SOURCE_PDF = get_sample_file_path("source.pdf")
TARGET_PDF = get_sample_file_path("target.pdf")
TARGET2_PDF = get_sample_file_path("target2.pdf")
TARGET3_PDF = get_sample_file_path("target3.pdf")

SOURCE_WITH_FOOTER = get_sample_file_path("sourceWithFooter.docx")
TARGET_WITH_FOOTER = get_sample_file_path("targetWithFooter.docx")

SOURCE_COMPARE_OPTIONS = get_sample_file_path("source_compare_options.docx")
TARGET_COMPARE_OPTIONS = get_sample_file_path("target_compare_options.docx")

SOURCE_REVISIONS = get_sample_file_path("revision.docx")

SOURCE_FOLDER = get_sample_file_path("SourceFolder")
TARGET_FOLDER = get_sample_file_path("TargetFolder")

RESULT_WORD = "result.docx"
RESULT_WITH_NEW_AUTHOR_WORD = "resultWithNewAuthor.docx"
RESULT_WITH_ACCEPTED_CHANGE_WORD = "resultWithAcceptedChange.docx"
RESULT_WITH_REJECTED_CHANGE_WORD = "resultWithRejectedChange.docx"
RESULT_WORD_FONT = "result_font.docx"

RESULT_TXT = "result.txt"
RESULT_PDF = "result.pdf"
RESULT_REVISIONS = "result.docx"
RESULT_FOLDER = "ResultFolderCompare"
