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

print(platform.system())

IL2CPU = "https://github.com/CosmosOS/IL2CPU.git"
XSharp = "https://github.com/CosmosOS/XSharp.git"
Cosmos = "https://github.com/CosmosOS/Cosmos.git"

gitupdate( Cosmos, "/Cosmos/")
gitupdate( IL2CPU, "/IL2CPU/")
gitupdate( XSharp, "/XSharp/")


root = os.getcwd()

subprocess.run(root + '\Cosmos\install-VS2017.bat -NOVSLAUNCH', cwd=root + '\Cosmos' )

print("Done :)")
os.system("pause")