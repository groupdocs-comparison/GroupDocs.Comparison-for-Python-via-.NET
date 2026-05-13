import io

from groupdocs.comparison.words.revision import RevisionHandler, RevisionAction, ApplyRevisionOptions

def accept_or_reject_revisions_stream():
    # NOTE: passing the raw file object returned by `open(path, 'rb')` causes
    # the wrapper to open a hidden .NET FileStream on `path` (via
    # BridgeHelper.OpenFile). RevisionHandler.Dispose() follows the standard
    # .NET caller-owned-stream convention and does NOT dispose that
    # FileStream, so the source file stays locked after the `with` block
    # exits and any subsequent example trying to open the same file fails
    # with "The process cannot access the file ... because it is being used
    # by another process". Reading the bytes into a BytesIO routes through
    # the MemoryStream path instead — no FileStream, no lock leak.
    with open("./Document_with_revision.docx", "rb") as f:
        source_stream = io.BytesIO(f.read())

    with RevisionHandler(source_stream) as revision_handler:
        revisions = revision_handler.get_revisions()
        for revision in revisions:
            if revision.type == "Insertion":
                revision.action = RevisionAction.ACCEPT

        options = ApplyRevisionOptions()
        options.changes = revisions
        revision_handler.apply_revision_changes("./result.docx", options)

if __name__ == "__main__":
    accept_or_reject_revisions_stream()
