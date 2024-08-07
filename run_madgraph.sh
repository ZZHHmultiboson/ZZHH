#!/bin/bash

# Searching for process definition

file="/afs/cern.ch/user/c/ccarriva/ZZHH/processes.json"

proc=$1
#mg5_string=""

isSignal=$(jq -r ".${proc}.isSignal" $file)
mg5_string=$(jq -r ".${proc}.mg5_syntax" $file)
BR=$(jq -r ".${proc}.BR" $file)
cuts=$(jq -r ".${proc}.cuts" $file)

if [ "$isSignal" == "null" ] || [ "$mg5_syntax" == "null" ] || [ "$BR" == "null" ]; then
    echo "No matching process found for $1"
    exit 1
fi

echo "isSignal: $isSignal"
echo "mg5_syntax: $mg5_string"
echo "BR: $BR"
echo "cuts: $cuts"

# Launching MadGraph

if [ "$isSignal" == "true" ]; then
  rm -r /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_${proc}*
  rm -r /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${proc}*
  mkdir /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_$proc
  mkdir /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_$proc/exe
else
  rm -r out_${proc}
fi

cmd_file="/afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/mg5_cmd.txt"

  if [ "$isSignal" == "true" ]; then
    echo "n" > $cmd_file
    echo "convert model /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/models/SM_Ltotal_Ind5v2020v2_UFO" >> $cmd_file
    echo "import model SM_Ltotal_Ind5v2020v2_UFO" >> $cmd_file
  else
    echo "import model sm" >> $cmd_file
  fi

  echo $mg5_string >> $cmd_file
  echo "output /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_$proc" >> $cmd_file
  echo "quit" >> $cmd_file

python3 /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/bin/mg5_aMC $cmd_file > /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/mg5_${proc}.log

cat $cmd_file
rm $cmd_file

operators_json="/afs/cern.ch/user/c/ccarriva/ZZHH/operators.json"
operators=()
for key in $(jq -r 'keys[]' "$operators_json"); do
  value=$(jq -r ".${key}.turn" "$operators_json")
  echo "Operator: $key, Turn: $value" # Debugging line
  if [ "$value" == "on" ]; then
    operators+=("$key")
  fi
done

echo "Operators: ${operators[@]}"

if [ "$isSignal" == "true" ]; then
  for oppe in ${operators[@]}
  do
    cp -r /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_$proc /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_${proc}_${oppe}
    cp /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/cuts/dummy_fct_${cuts}.f /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_${proc}_${oppe}/SubProcesses/dummy_fct.f
    source /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_sign/sendOne_cuts.sh out_${proc} $oppe
  done
else
  cp /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/cuts/dummy_fct_${cuts}.f /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_$proc/SubProcesses/dummy_fct.f
  source /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/condor_bkg/sendOne_cuts_bkg.sh out_$proc
fi

exit 0
