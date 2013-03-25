#!/usr/bin/python
import os
from subprocess import call
call(["svn","co","https://sframe.svn.sourceforge.net/svnroot/sframe/SFrame/tags/SFrame-03-05-16","SFrame"])
os.chdir("SFrame/core") 
call(["cat","Makefile"])
f = open("Makefile")
file = f.read()
newfile = file.replace("lpcre -o","o")
open("Makefile", "w").write(newfile)
call(["source","setup.sh"])
call(["make", "-j","10"])




