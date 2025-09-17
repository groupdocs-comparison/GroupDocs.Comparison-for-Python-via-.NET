import os
from groupdocs.comparison.words.revision import RevisionHandler, RevisionType, RevisionAction, ApplyRevisionOptions
import constants as c  # your constants.py

def accept_reject_revisions_from_path():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # AcceptRejectRevisionsFromPath : how to get revisions from document path\n")

    # Paths for accepted and rejected revisions
    output_dir_accepted = os.path.join(c.outputPath, "AcceptRevisionsFromPath")
    os.makedirs(output_dir_accepted, exist_ok=True)
    output_file_accepted = os.path.join(output_dir_accepted, c.RESULT_REVISIONS)

    output_dir_rejected = os.path.join(c.outputPath, "RejectRevisionsFromPath")
    os.makedirs(output_dir_rejected, exist_ok=True)
    output_file_rejected = os.path.join(output_dir_rejected, c.RESULT_REVISIONS)

    # Accept some changes
    with RevisionHandler(c.SOURCE_REVISIONS) as revision_handler:
        revision_list = revision_handler.get_revisions()
        for rev in revision_list:
            if rev.type == RevisionType.INSERTION:
                rev.action = RevisionAction.ACCEPT

        revision_handler.apply_revision_changes(output_file_accepted,
                                                ApplyRevisionOptions(changes=revision_list))

    # Reject some changes
    with RevisionHandler(c.SOURCE_REVISIONS) as revision_handler:
        revision_list = revision_handler.get_revisions()
        for rev in revision_list:
            if rev.type == RevisionType.INSERTION:
                rev.action = RevisionAction.REJECT

        revision_handler.apply_revision_changes(output_file_rejected,
                                                ApplyRevisionOptions(changes=revision_list))

    print(f"\nRevisions processed successfully.\nCheck output in {os.getcwd()}.")


def accept_reject_revisions_from_stream():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # AcceptRejectRevisionsFromStream : how to get revisions from document stream\n")

    # Accept revisions
    output_dir_accepted = os.path.join(c.outputPath, "AcceptRevisionsFromStream")
    os.makedirs(output_dir_accepted, exist_ok=True)
    output_file_accepted = os.path.join(output_dir_accepted, c.RESULT_REVISIONS)

    with open(c.SOURCE_REVISIONS, "rb") as source_stream:
        with RevisionHandler(source_stream) as revision_handler:
            revision_list = revision_handler.get_revisions()
            for rev in revision_list:
                if rev.type == RevisionType.INSERTION:
                    rev.action = RevisionAction.ACCEPT

            with open(output_file_accepted, "wb") as result_stream:
                revision_handler.apply_revision_changes(result_stream,
                                                        ApplyRevisionOptions(changes=revision_list))

    # Reject revisions
    output_dir_rejected = os.path.join(c.outputPath, "RejectRevisionsFromStream")
    os.makedirs(output_dir_rejected, exist_ok=True)
    output_file_rejected = os.path.join(output_dir_rejected, c.RESULT_REVISIONS)

    with open(c.SOURCE_REVISIONS, "rb") as source_stream:
        with RevisionHandler(source_stream) as revision_handler:
            revision_list = revision_handler.get_revisions()
            for rev in revision_list:
                if rev.type == RevisionType.INSERTION:
                    rev.action = RevisionAction.REJECT

            with open(output_file_rejected, "wb") as result_stream:
                revision_handler.apply_revision_changes(result_stream,
                                                        ApplyRevisionOptions(changes=revision_list))

    print(f"\nRevisions processed successfully.\nCheck output in {os.getcwd()}.")


def accept_reject_all_revisions():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # AcceptRejectAllRevisions : how to optimally handle all revisions\n")

    output_dir_accepted = os.path.join(c.outputPath, "AcceptAllRevisions")
    os.makedirs(output_dir_accepted, exist_ok=True)
    output_file_accepted = os.path.join(output_dir_accepted, c.RESULT_REVISIONS)

    output_dir_rejected = os.path.join(c.outputPath, "RejectAllRevisions")
    os.makedirs(output_dir_rejected, exist_ok=True)
    output_file_rejected = os.path.join(output_dir_rejected, c.RESULT_REVISIONS)

    # Accept all changes
    with RevisionHandler(c.SOURCE_REVISIONS) as revision_handler:
        revision_handler.apply_revision_changes(output_file_accepted,
                                                ApplyRevisionOptions(common_handler=RevisionAction.ACCEPT))

    # Reject all changes
    with RevisionHandler(c.SOURCE_REVISIONS) as revision_handler:
        revision_handler.apply_revision_changes(output_file_rejected,
                                                ApplyRevisionOptions(common_handler=RevisionAction.REJECT))

    print(f"\nRevisions processed successfully.\nCheck output in {os.getcwd()}")


if __name__ == "__main__":
    accept_reject_revisions_from_path()
    accept_reject_revisions_from_stream()
    accept_reject_all_revisions()
