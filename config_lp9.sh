#!/bin/bash
# Launch this script from your work directory

# CMSSW release
(
echo "Setting up CMSSW_13_0_16..."
cmsrel CMSSW_13_0_16
cd CMSSW_13_0_16/src/
cmsenv
cd ../..

# MadGraph and Eboli model
echo "Downloading MG5_aMC_v2_9_18..."
wget http://cms-project-generators.web.cern.ch/cms-project-generators/MG5_aMC_v2.9.18.tar.gz
tar xvf MG5_aMC_v2.9.18.tar.gz

echo "Searching for Eboli model..."
cd MG5_aMC_v2_9_18/models/
cp ../../scripts/models/sm_Eboli.tgz .
tar xvf sm_Eboli.tgz
rm sm_Eboli.tgz
cd ../../CMSSW_13_0_16/
eval `scram runtime -sh` scram tool info lhapdf
LHAPDF_DATA_PATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lhapdf/6.2.1-nmpfii3/share/LHAPDF
cd ../MG5_aMC_v2_9_18/
export LHAPDF_DATA_PATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lhapdf/6.2.1-nmpfii3/share/LHAPDF
)

# First set of scripts
rm MG5_aMC_v2.9.18.tar.gz
mkdir Plots
mkdir Output
baseDir=$(pwd)
echo $baseDir
pyPath="$(echo $baseDir | sed "s|/|', '|g" | cut -c5-)'"
echo $pyPath

find . -type f -exec sed -i "s|/afs/cern.ch/user/c/ccarriva/ZZHH|$baseDir|g" {} +
find . -type f -exec sed -i "s|afs', 'cern.ch', 'user', 'c', 'ccarriva', 'ZZHH'|$pyPath|g" {} +
#sed -i "s|afs', 'cern.ch', 'user', 'c', 'ccarriva', 'ZZHH'|$pyPath|g" plot_and_compute_fractions_checkCuts.py
#sed -i "s|afs', 'cern.ch', 'user', 'c', 'ccarriva', 'ZZHH'|$pyPath|g" plot_only.py

#cd ../MG5_aMC_v2_9_18
#cp ../scripts/condor/MG5config_generic_cuts.txt .
#cp ../scripts/condor/copyandsend_generic_cuts.sh .
#cp ../scripts/condor/condor_cuts.sub .
#cp ../scripts/condor/sendOne_cuts.sh .
#cp ../scripts/createCsv.sh .
#cp ../scripts/my_analyzer_cuts.py .
#cp ../scripts/run_madgraph.sh .

# Plots repository
echo "Setting up plotting enviroment..."
cd Plots

cp ../scripts/plot_and_compute_fractions_checkCuts.py .
cp ../scripts/my_analyzer_unitarity.py .
cp ../scripts/unitarity_estimate.py .
cp ../scripts/plot_only.py .
cp ../scripts/limits_compare.py .

python3 -m venv myenv
source myenv/bin/activate
myenv/bin/python -m pip install --upgrade pip
pip install numpy matplotlib cycler hist lhereader
deactivate
