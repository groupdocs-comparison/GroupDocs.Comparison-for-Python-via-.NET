# set_metered_license.py
# This example demonstrates how to set a Metered license.
# Learn more about Metered license at https://purchase.groupdocs.com/faqs/licensing/metered.

import groupdocs.comparison as gc

def run():
    public_key = "*****"  # Your public key
    private_key = "*****"  # Your private key

    gc.Metered().set_metered_key(public_key, private_key)

    print("License set successfully.")

if __name__ == "__main__":
    run()
