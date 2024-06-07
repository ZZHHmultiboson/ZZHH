#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

cd /afs/cern.ch/user/c/ccarriva/rareH_el9/CMSSW_13_0_16
eval `scram runtime -sh`
cd -
cp -r /afs/cern.ch/user/c/ccarriva/rareH_el9/MG5_aMC_v2_9_18 .
cd MG5_aMC_v2_9_18
python3 bin/mg5_aMC file_${1}_${2}.txt
cp -r ${1}/Events/run_${2}_* /afs/cern.ch/user/c/ccarriva/rareH_el9/MG5_aMC_v2_9_18/${1}/Events/
