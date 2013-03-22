#!/usr/bin/python
import os
from subprocess import call
call(["mkdir","-p","fastjet/tarfiles"])
os.chdir("fastjet/tarfiles")
call(["curl","-O","fastjet.fr/repo/fastjet-3.0.2.tar.gz"])
call(["tar","xfz","fastjet-3.0.2.tar.gz"])
call(["mv","fastjet-3.0.2","../3.0.2"])
os.chdir("../3.0.2")
call(["./configure","--prefix="+os.getcwd()+"/../3.0.2-install"])
call(["make","-j","10"])
call(["make","install"])

