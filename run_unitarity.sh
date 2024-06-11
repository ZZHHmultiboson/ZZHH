#!/bin/bash

proc=$1
cuts=$2
ref_op=$3
operators=("FM0" "FM1" "FM2" "FM3" "FM4" "FM5" "FM7" "FS0" "FS1" "FS2")
values=("0" "minus20" "minus10" "minus5" "minus2" "2" "5" "10" "20")
mkdir Output/$1/unitarityPlots

cd Plots
source myenv/bin/activate
for oppe in ${operators[@]}
do
    for value in ${values[@]}
    do
        echo "Running operator $oppe, value $value ..."
        python3 plot_and_compute_fractions_checkCuts.py $proc $oppe $value
    done
done
deactivate

cd ../CMSSW_13_0_16/src
cmsenv
cd -
python3 my_analyzer_unitarity.py $proc m1100
python3 unitarity_estimate.py $proc $cuts $ref_op
python3 limits_compare.py $proc

exit 0