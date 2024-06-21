#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

file="/afs/cern.ch/user/c/ccarriva/ZZHH/processes.json"
proc=$1

isSignal=$(jq -r ".${proc}.isSignal" $file)

operators=()

for key in $(jq -r 'keys[]' /afs/cern.ch/user/c/ccarriva/ZZHH/operators.json); do
  value=$(jq -r ".${key}" /afs/cern.ch/user/c/ccarriva/ZZHH/operators.json)
  if [ "$value" == "on" ]; then
    operators+=("$key")
  fi
done

if [ "$isSignal" == "false" ]; then
  more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/run_out_${1}_cuts.out | grep "Cross-sect" | head -1 | sed "s#     Cross-section :   #0.,#g" | sed "s# +- #,#g" | sed "s#pb##g" > /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}.csv
else
  for oppe in ${operators[@]} 
    do
    more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${1}/run_out_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -1 | sed "s#     Cross-section :   #0.,#g" | sed "s# +- #,#g" | sed "s#pb##g" > /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}_${oppe}.csv
    more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${1}/run_out_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -2 | tail -1 | sed "s#     Cross-section :   #-20.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}_${oppe}.csv
    more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${1}/run_out_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -3 | tail -1 | sed "s#     Cross-section :   #-10.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}_${oppe}.csv
    more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${1}/run_out_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -4 | tail -1 | sed "s#     Cross-section :   #-5.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}_${oppe}.csv
    more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${1}/run_out_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -5 | tail -1 | sed "s#     Cross-section :   #-2.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}_${oppe}.csv
    more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${1}/run_out_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -6 | tail -1 | sed "s#     Cross-section :   #2.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}_${oppe}.csv
    more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${1}/run_out_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -7 | tail -1 | sed "s#     Cross-section :   #5.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}_${oppe}.csv
    more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${1}/run_out_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -8 | tail -1 | sed "s#     Cross-section :   #10.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}_${oppe}.csv
    more /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_${1}/run_out_${1}_${oppe}_cuts.out | grep "Cross-sect" | tail -1 | sed "s#     Cross-section :   #20.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/${2}/model_Eboli_${1}_${oppe}.csv
  done
fi
