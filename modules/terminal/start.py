# Terminal module - start

import sys
import json
import subprocess

if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    root = "/opt/braintux-master"
elif sys.platform == "nt":
    root = r"%ProgramFiles%/braintux-master"

with open('{}/config.json'.format(root)) as f:

    data = json.load(f)

    if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":

        if data["my_linux_terminal"] != "":
            new_window_command = data["my_linux_terminal"]
        else:
            new_window_command = data["default_linux_terminal"]
        
    elif sys.platform == "nt":

        if data["my_windows_terminal"] != "":
            new_window_command = data["my_windows_terminal"]
        else:
            new_window_command = data["default_windows_terminal"]

subprocess.Popen("{} 'python3 {}/modules/terminal/terminal.py' >/dev/null 2>&1;".format(new_window_command, root), shell=True)