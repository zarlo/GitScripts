#!/usr/bin/python

import subprocess
import os.path
import platform

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def Restore(*args):
    return subprocess.check_call(['dotnet', 'restore'] + list(args))

print(platform.system())

IL2CPU = "https://github.com/CosmosOS/IL2CPU.git"
XSharp = "https://github.com/CosmosOS/XSharp.git"
Cosmos = "https://github.com/CosmosOS/Cosmos.git"

if os.path.exists('Cosmos/') == False:
    git("clone", Cosmos, "Cosmos/")
else:
    git("pull", Cosmos, "Cosmos/")

if os.path.exists('IL2CPU/') == False:
    git("clone", IL2CPU, "IL2CPU/")
else:
    git("pull", IL2CPU, "IL2CPU/")

if os.path.exists('XSharp/') == False:
    git("clone", XSharp, "XSharp/")
else:
    git("pull", XSharp, "XSharp/")


if platform.system() == Windows:
    subprocess.check_call(['CMD.exe', 'Cosmos/install-VS2017.bat'])
else:
    Restore("Cosmos/Builder.sln")
