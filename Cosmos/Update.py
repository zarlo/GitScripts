#!/usr/bin/python

import subprocess
import os.path
import platform
import hashlib
import urllib2

def DownloadUpdater():
    Updater = urllib2.urlopen("https://raw.githubusercontent.com/zarlo/GitScripts/master/UpdaterScript.py")
    NewFile = open("Updater.py", 'w')
    NewFile.write(Updater.read())
    NewFile.close()

def RunUpdater():
    return os.system("Updater.py https://raw.githubusercontent.com/zarlo/GitScripts/master/Cosmos/Update.py " + __file__)


def git(*args):
    return subprocess.check_call(['git'] + list(args))

def gitupdate(repo, mPath):
    if os.path.exists(mPath) == False and os.path.exists(mPath + "/.git" == True):
        git("clone", repo, mPath)
    else:
        git("pull", repo, mPath)

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()

def sha256_checksum_Remote(url, block_size=65536):
    sha256 = hashlib.sha256()
    remote = urllib2.urlopen(url)

    while True:

        data = remote.read(4096)

        if not data:
            break

        sha256.update(data)

    return sha256.hexdigest()


print(platform.system())

print("Looking for script update")

ScriptvL = sha256_checksum(os.path.basename(__file__));
ScriptvR = sha256_checksum_Remote("https://raw.githubusercontent.com/zarlo/GitScripts/master/Cosmos/Update.py");


print("Loacl: " + ScriptvL)
print("Remote: " + ScriptvR)

if ScriptvR != ScriptvL:
   DownloadUpdater()
   RunUpdater()
else:

   IL2CPU = "https://github.com/CosmosOS/IL2CPU.git"
   XSharp = "https://github.com/CosmosOS/XSharp.git"
   Cosmos = "https://github.com/CosmosOS/Cosmos.git"

   gitupdate( Cosmos, "Cosmos/")
   gitupdate( IL2CPU, "IL2CPU/")
   gitupdate( XSharp, "XSharp/")


   subprocess.check_call(['CMD.exe', 'Cosmos/install-VS2017.bat  -NOVSLAUNCH'])

   print("Done :)")
   os.system("pause")
