#!/usr/bin/python

import sys
import urllib2

remote = urllib2.urlopen(sys.argv[1])
NewFile = open(sys.argv[2], 'w')
NewFile.write(remote.read())
NewFile.close()
