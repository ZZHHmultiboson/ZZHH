#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }
echo "Start of job on " `date`
cat /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_bkg/MG5config_generic_cuts_bkg.txt | sed "s#SIGNAL#${1}#g" > /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/file_${1}.txt
cat /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_bkg/condor_cuts_bkg.sub | sed "s#SIGNAL#${1}#g" > /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_${1}_cuts.sub
condor_submit /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_${1}_cuts.sub
