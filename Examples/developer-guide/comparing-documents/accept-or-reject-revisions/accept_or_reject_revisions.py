from groupdocs.comparison.words.revision import RevisionHandler, RevisionAction, ApplyRevisionOptions

def accept_or_reject_revisions():
    with RevisionHandler("./Document_with_revision.docx") as revision_handler:
        revisions = revision_handler.get_revisions()
        for revision in revisions:
            if revision.type == "Insertion":
                revision.action = RevisionAction.ACCEPT
            else:
                revision.action = RevisionAction.REJECT

        options = ApplyRevisionOptions()
        options.changes = revisions
        revision_handler.apply_revision_changes("./result.docx", options)

if __name__ == "__main__":
    accept_or_reject_revisions()