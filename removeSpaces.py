#!/usr/bin/env python

import sys
import subprocess
import re
from os import listdir

folder = sys.argv[1]
file_list = listdir(folder)

for file_name in file_list:
	subprocess.call("mv " + folder + "/" + re.sub("\s", "\\ ", file_name) + " " + folder + "/" + re.sub("\s", "_", file_name), shell=True)