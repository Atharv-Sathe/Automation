'''
WARNING: This script will delete all the files in the 'Generated' folder.
'''

# Python Script to delete all the generated files from the 'Generated' folder.

import os
import glob

files = glob.glob('./Generated/*')
for f in files:
    os.remove(f)

print('BlackHole Protocol Completed!')