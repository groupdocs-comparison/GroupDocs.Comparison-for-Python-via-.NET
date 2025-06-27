# set_license_from_file.py
# This example demonstrates how to set license from file.
# The SetLicense method attempts to set a license from several locations relative to the executable and GroupDocs.Comparison.dll.
# You can also use the additional overload to load a license from a stream, this is useful for instance when the 
# License is stored as an embedded resource. 

import groupdocs.comparison as gc
import utils
import os
  

def run():
    if os.path.exists(utils.license_path):    
        license = gc.License()
        license.set_license(utils.license_path)
        print("License set successfully.")
    else:
       print("\n")


