# Qt module - start

import os
import sys
import json
import subprocess

if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    root = "/opt/braintux-master"
elif sys.platform == "nt":
    root = r"%ProgramFiles%/braintux-master"

subprocess.Popen("python3 {}/modules/qt/qt.py >/dev/null 2>&1;".format(root), shell=True)