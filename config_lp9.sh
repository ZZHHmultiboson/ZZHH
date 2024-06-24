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

# Plots repository
echo "Setting up plotting enviroment..."
#cp ../scripts/plot_and_compute_fractions_checkCuts.py .
#cp ../scripts/my_analyzer_unitarity.py .
#cp ../scripts/unitarity_estimate.py .
#cp ../scripts/limits_compare.py .
#cp ../scripts/plot_only.py .

python3 -m venv myenv
source myenv/bin/activate
myenv/bin/python -m pip install --upgrade pip
pip install tensorflow==2.6.4
pip install absl-py~=0.10
pip install clang~=5.0
pip install flatbuffers~=1.12.0
pip install gast==0.4.0
pip install h5py~=3.1.0
pip install numpy~=1.19.2
pip install opt-einsum~=3.3.0
pip install six~=1.15.0
pip install tensorboard<2.7,>=2.6.0
pip install tensorflow-estimator<2.7,>=2.6.0
pip install typing-extensions<3.11,>=3.7
pip install wrapt~=1.12.1
pip install numpy matplotlib cycler hist lhereader
deactivate
