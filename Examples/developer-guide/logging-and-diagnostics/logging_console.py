from groupdocs.comparison import Comparer, ComparerSettings
from groupdocs.comparison.logging import ConsoleLogger

def logging_console():
    settings = ComparerSettings()
    settings.logger = ConsoleLogger()

    with Comparer("./source.docx", settings=settings) as comparer:
        comparer.add("./target.docx")
        comparer.compare("./result.docx")

if __name__ == "__main__":
    logging_console()