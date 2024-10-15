#!/bin/bash

file="/afs/cern.ch/user/c/covarell/work/mg5_amcatnlo/dim8-new/ZZHH/processes.json"

proc=$1
numbjets=$2
numleptons=$3

isSignal=$(jq -r ".${proc}.isSignal" $file)

# Moving results to outDir

cd CMSSW_13_0_16/src
eval `scram runtime -sh`
mkdir -p GenProd
mkdir -p GenProd/Test
mkdir -p GenProd/Test/python
cd GenProd/Test/python
cp ../../../../../acceptance_template_cfg.py .
sed -i -e "s#MYBJ#${2}#" acceptance_template_cfg.py
sed -i -e "s#MYLEPT#${3}#" acceptance_template_cfg.py
cd -
scram b
cd ../..

if [ "$isSignal" == "true" ]; then
  cmsDriver.py GenProd/Test/python/acceptance_template_cfg.py --filein "file:./Output/$1/xsec/Events/run_FM0_0_cuts/unweighted_events.lhe" --python_filename acceptance_$1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --fileout file:pythia_$1.root --conditions 133X_mcRun3_2024_realistic_v6 --beamspot Realistic25ns13p6TeVEarly2023Collision --step GEN --geometry DB:Extended --era Run3_2023 --no_exec --mc -n 100000 
else
  cmsDriver.py GenProd/Test/python/acceptance_template_cfg.py --filein "file:./Output/$1/xsec/Events/run_SMbkg_0_cuts/unweighted_events.lhe" --python_filename acceptance_$1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --fileout file:pythia_$1.root --conditions 133X_mcRun3_2024_realistic_v6 --beamspot Realistic25ns13p6TeVEarly2023Collision --step GEN --geometry DB:Extended --era Run3_2023 --no_exec --mc -n 100000   
fi

cmsRun acceptance_$1_cfg.py &> acceptance_$1.txt

exit 0
