#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }
echo "Start of job on " `date`
cd /afs/cern.ch/user/c/ccarriva/ZZHH/CMSSW_13_0_16
eval `scram runtime -sh`
cd /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18
python3 /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/bin/mg5_aMC /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/file_${1}.txt
