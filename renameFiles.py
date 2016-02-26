#!/usr/bin/env python
# execute ./renameFiles.py PATH/TO/DIRECTORY STRING-TO-BE-REPLACED(optional) REPLACER(optional)
# default replaces spaces with _'s if optional arguments are not supplied

import sys
print(sys.argv[1])
import subprocess
import re
from os import listdir

folder = sys.argv[1]
file_list = listdir(folder)
replace = sys.argv[2]
if sys.argv[3] == ' ':
	replacer = '\\ '
else:
	replacer = sys.argv[3]

for file_name in file_list:
	subprocess.call("mv " + folder + "/" + re.sub("\s", "\\ ", file_name) + " " + folder + "/" + re.sub(replace, replacer, file_name.lower()) if len(sys.argv) > 2 else re.sub("\s", "_", file_name.lower()), shell=True)