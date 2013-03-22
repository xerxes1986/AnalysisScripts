#!/usr/bin/python
import os
from subprocess import call
os.environ["SCRAM_ARCH"] = "slc5_amd64_gcc462"
call(["scram","project","CMSSW","CMSSW_5_3_3"])
os.chdir("CMSSW_5_3_3/src")
os.system("eval `scramv1 runtime -sh`")
os.environ["CVSROOT"] = ":pserver:anonymous@cmssw.cvs.cern.ch:/local/reps/CMSSW"
call(["cvs","co","-d","UHHAnalysis/NtupleWriter","-r","Dec-05-2012-v1","UserCode/UHHAnalysis/NtupleWriter"])
call(["cvs","co","-d","EGamma/EGamma/AnalysisTools","-r","V00-00-08","UserCode/EGamma/EGammaAnalysisTools"])
call(["scram","b","-j","10"])
