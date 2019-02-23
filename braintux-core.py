#!/usr/bin/env python3

# Default imports
import os, sys, subprocess
from views.term import Term
term = Term()

if sys.argv[1] == "start":
    # Start a module
    if sys.argv[2] == "whatsapp":
        # Importing whatsapp
        #subprocess.Popen("python3 views/whatsapp.py '"+sys.argv[3]+"' '"+sys.argv[4]+"'")
        p = subprocess.Popen('python3 views/whatsapp.py'+"'"+sys.argv[3]+"'"+"'"+sys.argv[4]+"'"+' >/dev/null 2>&1', shell=True)
        subprocess.call("echo lolo", shell=True)
        print('ta rodando em segundo plano, bicho')