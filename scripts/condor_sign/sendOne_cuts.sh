#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

opnum=0
if [[ "$2" == "FS0" ]]
then
  opnum=1
elif [[ "$2" == "FS1" ]]
then
  opnum=2
elif [[ "$2" == "FS2" ]]
then
  opnum=3
elif [[ "$2" == "FM0" ]]
then
  opnum=4
elif [[ "$2" == "FM1" ]]
then
  opnum=5
elif [[ "$2" == "FM2" ]]
then
  opnum=6
elif [[ "$2" == "FM3" ]]
then
  opnum=7
elif [[ "$2" == "FM4" ]]
then
  opnum=8
elif [[ "$2" == "FM5" ]]
then
  opnum=9
elif [[ "$2" == "FM6" ]]
then
  opnum=10
elif [[ "$2" == "FM7" ]]
then
  opnum=11
fi

cat /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_sign/MG5config_generic_cuts.txt | sed "s#SIGNAL#${1}#g" | sed "s#OPERAT#${2}#g" | sed "s#BABA#${opnum}#g" > /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_${1}/file_${1}_${2}.txt
cat /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_sign/condor_cuts.sub | sed "s#SIGNAL#${1}#g" | sed "s#OPERAT#${2}#g" > /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_${1}/condor_${1}_${2}_cuts.sub
cat /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_sign/copyandsend_generic_cuts.sh | sed "s#SIGNAL#${1}#g" | sed "s#OPERAT#${2}#g" > /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_${1}/exe/copyandsend_generic_cuts_${2}.sh
condor_submit /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_${1}/condor_${1}_${2}_cuts.sub
