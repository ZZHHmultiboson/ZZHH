#!/bin/bash

proc=$1
cuts=$2
#ref_op=$3

file="/afs/cern.ch/user/c/ccarriva/ZZHH/processes.json"
isSignal=$(jq -r ".${proc}.isSignal" $file)
if [ "$isSignal" == "false" ]; then 
  echo "Trying to run limits for a background process. Please provide a signal as input."
  exit 1
fi

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

values=("0" "minus20" "minus10" "minus5" "minus2" "2" "5" "10" "20")
mkdir /afs/cern.ch/user/c/ccarriva/ZZHH/Output/$1/unitarityPlots

source /afs/cern.ch/user/c/ccarriva/ZZHH/myenv/bin/activate
echo "Python executable: $(which python3)"
for oppe in ${operators[@]}
do
  for value in ${values[@]}
  do
    echo "Running operator $oppe, value $value ..."
    python3 /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/plot_and_compute_fractions_checkCuts.py $proc $oppe $value
  done
done
deactivate

cd /afs/cern.ch/user/c/ccarriva/ZZHH/CMSSW_13_0_16/src
cmsenv
cd -
python3 /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/my_analyzer_unitarity.py $proc m1100
# python3 /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/unitarity_estimate.py $proc $cuts $ref_op
python3 /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/unitarity_estimate_fromSplusB.py $proc $cuts
python3 /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/limits_compare.py $proc

exit 0