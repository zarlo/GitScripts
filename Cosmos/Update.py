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

IL2CPU = "https://github.com/CosmosOS/IL2CPU.git"
XSharp = "https://github.com/CosmosOS/XSharp.git"
Cosmos = "https://github.com/CosmosOS/Cosmos.git"

gitupdate( Cosmos, "Cosmos/")
gitupdate( IL2CPU, "IL2CPU/")
gitupdate( XSharp, "XSharp/")


if platform.system() == Windows:
    subprocess.check_call(['CMD.exe', 'Cosmos/install-VS2017.bat'])
else:
    Restore("Cosmos/Builder.sln")
