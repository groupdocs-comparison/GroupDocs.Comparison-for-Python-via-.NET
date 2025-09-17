import os
from groupdocs.comparison import Comparer, Metered
from groupdocs.comparison.options import SaveOptions, CompareOptions
import constants as c  # your constants.py

def run():
    print("\n" + "-" * 116)
    print("[Example Advanced Usage] # GetMeteredCreditsLimit : how to get credit consumption quantity\n")

    print(f"Credits before using Comparer: {Metered.get_consumption_quantity()}")

    output_file = c.RESULT_WORD
    with open(output_file, "wb") as result_stream:
        with Comparer(c.SOURCE_WORD) as comparer:
            comparer.add(c.TARGET_WORD)
            comparer.compare(result_stream, SaveOptions(), CompareOptions())

    print(f"Credits after using Comparer: {Metered.get_consumption_quantity()}")
    print(f"\nDocuments compared successfully.\nCheck output in {os.getcwd()}")


if __name__ == "__main__":
    run()
