#!/bin/bash

# Searching for process definition

file="/afs/cern.ch/user/c/ccarriva/ZZHH/processes.json"

proc=$1
#mg5_string=""

isSignal=$(jq -r ".${proc}.isSignal" $file)
mg5_string=$(jq -r ".${proc}.mg5_syntax" $file)
BR=$(jq -r ".${proc}.BR" $file)

if [ "$isSignal" == "null" ] || [ "$mg5_syntax" == "null" ] || [ "$BR" == "null" ]; then
    echo "No matching process found for $1"
    exit 1
fi

echo "isSignal: $isSignal"
echo "mg5_syntax: $mg5_string"
echo "BR: $BR"

# Launching MadGraph

rm -r out_$proc
cmd_file="/afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/mg5_cmd.txt"

  echo "n" > $cmd_file

  if [ "$isSignal" == "true" ]; then
    echo "convert model /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/models/SM_Ltotal_Ind5v2020v2_UFO" >> $cmd_file
    echo "import model SM_Ltotal_Ind5v2020v2_UFO" >> $cmd_file
  else
    echo "import model sm" >> $cmd_file
  fi

  echo $mg5_string >> $cmd_file
  echo "output /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_$proc" >> $cmd_file
  echo "quit" >> $cmd_file

python3 /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/bin/mg5_aMC $cmd_file > /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/mg5_$proc.log

cat $cmd_file
rm $cmd_file
rm /afs/cern.ch/user/c/ccarriva/ZZHH/py.py

if [ "$isSignal" == "true" ]; then
  cp /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_sign/dummy_fct_forWZ.f /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_$proc/SubProcesses/dummy_fct.f
else
  cp /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_bkg/dummy_fct_ppTozbbbb.f /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_$proc/SubProcesses/dummy_fct.f
fi

# Launching jobs for Cross Section on condor

operators=("FS0" "FS1" "FS2" "FM0" "FM1" "FM2" "FM3" "FM4" "FM5" "FM7")
if [ "$isSignal" == "true" ]; then
  for operator in "${operators[@]}"; do
    source /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_sign/sendOne_cuts.sh out_$proc $operator
  done
else
  source /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_bkg/sendOne_cuts_bkg.sh out_$proc
fi

exit 0