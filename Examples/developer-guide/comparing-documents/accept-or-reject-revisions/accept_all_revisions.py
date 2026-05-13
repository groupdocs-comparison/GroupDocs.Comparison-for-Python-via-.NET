from groupdocs.comparison.words.revision import RevisionHandler, RevisionAction, ApplyRevisionOptions

def accept_all_revisions():
    with RevisionHandler("./Document_with_revision.docx") as revision_handler:
        options = ApplyRevisionOptions()
        options.common_handler = RevisionAction.ACCEPT
        revision_handler.apply_revision_changes("./result.docx", options)

if __name__ == "__main__":
    accept_all_revisions()