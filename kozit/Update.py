#!/usr/bin/python

import subprocess
import os.path
import platform

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def gitupdate(repo, mPath):
    if os.path.exists(mPath) == False:
        git("clone", repo, mPath)
    else:
        git("pull", repo, mPath)

def Restore(*args):
    return subprocess.check_call(['dotnet', 'restore'] + list(args))

print(platform.system())

gitupdate("https://github.com/kozit/kozit.git", "kozit/")

gitupdate("https://github.com/kozit/kozitScript.git", "kozitScript/")

gitupdate("https://github.com/kozit/libraries.git", "libraries/")

gitupdate("https://github.com/kozit/installer.git", "installer/")
