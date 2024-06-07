#!/bin/bash
# Launch this script from your work directory

# CMSSW release
echo "Setting up CMSSW_13_0_16..."
cmsrel CMSSW_13_0_16
cd CMSSW_13_0_16/src/
cmsenv
cd ../..

# Central Repository
git clone git@github.com:acappati/ZZH.git
git clone -b ZZHHpaper git@github.com:acappati/mg5tut_apr21_plots.git
# Il clone in teoria chiede la password, questi potrebbero non essere automatici!!!
# si può evitare questo problema lasciando gli script base in una cartella che non è un clone, e già dentro Multiboson_dim8

# MadGraph and Eboli model
echo "Downloading MG5_aMC_v2_9_18..."
mkdir test
cd test
wget http://cms-project-generators.web.cern.ch/cms-project-generators/MG5_aMC_v2.7.3.py3.tar.gz
tar xvf MG5_aMC_v2.9.18.tar.gz

echo "Searching for Eboli model..."
cd MG5_aMC_v2_9_18/models/
cp ../../../ZZH/models/sm_Eboli.tgz .
tar xvf sm_Eboli.tgz
cd ../../CMSSW_13_0_16/
eval `scram runtime -sh` scram tool info lhapdf
LHAPDF_DATA_PATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lhapdf/6.2.1-nmpfii3/share/LHAPDF
cd ../test/MG5_aMC_v2_9_18/
export LHAPDF_DATA_PATH=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lhapdf/6.2.1-nmpfii3/share/LHAPDF

# First set of scripts
cp ../../ZZH/condor/MG5config_generic_cuts.txt .
sed -i '/set mmjj 500.0/d' MG5config_generic_cuts.txt
sed -i '/set deltaeta 2.5/d' MG5config_generic_cuts.txt
sed -i '/set ptj 40.0/d' MG5config_generic_cuts.txt
sed -i '/set etaj 4.7/d' MG5config_generic_cuts.txt
cp ../../ZZH/condor/copyandsend_generic_cuts.sh .
cp ../../ZZH/condor/condor_cuts.sub .
cp ../../ZZH/condor/sendOne_cuts.sh .
cp ../../ZZH/createCsv.sh .

baseDir=$(echo $(pwd) | awk -F'/' 'BEGIN {OFS="/"} {for (i=1; i<=NF-2; i++) path = path OFS $i; sub("^/", "", path); print path}')
baseDir="$baseDir/"
echo $baseDir
sed -i "s|/afs/cern.ch/work/c/covarell/mg5_amcatnlo/dim8-hh/|$baseDir|g; s|/CMSSW_11_0_1|/CMSSW_13_0_16|g; s|/MG5_aMC_v2_7_3_py3|/test/MG5_aMC_v2_9_18|g; s|python|python3|g" copyandsend_generic_cuts.sh
sed -i '/cp ../../ZZH/dummy_fct_forWZ.f ${1}/SubProcesses/dummy_fct.f/d' copyandsend_generic_cuts.sh

# Plots repository
echo "Setting up plotting enviroment..."
cd ../mg5tut_apr21_plots
python3 -m venv myenv
source myenv/bin/activate
myenv/bin/python -m pip install --upgrade pip
pip install numpy matplotlib cycler hist lhereader
deactivate




