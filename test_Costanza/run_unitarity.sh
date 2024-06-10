#!/bin/bash

cd Plots

operators=("FM0" "FM1" "FM2" "FM3" "FM4" "FM5" "FM7" "FS0" "FS1" "FS2")
values=("0" "minus20" "minus10" "minus5" "minus2" "2" "5" "10" "20")

for oppe in ${operators[@]}
do
    for value in ${values[@]}
    do
        echo "running operator $oppe value $value ..."
        python3 plot_and_compute_fractions_checkCuts.py out_process3_ppTozhh $oppe $value
    done
done
