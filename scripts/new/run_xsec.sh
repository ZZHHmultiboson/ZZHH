#!/bin/bash

proc=$1

err_files=()
for file in /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/*.err; do
    if [[ "$file" == *"$1"* ]]; then
        err_files+=("$file")
    fi
done

# Checking if all jobs ended correctly

declare -a wrong_files
for err_file in "${err_files[@]}"; do
  while IFS= read -r line; do
      if [[ ! $line =~ ^[[:space:]]*0% && ! $line =~ ^[[:space:]]*100% && ! $line == "stty: 'standard input': Inappropriate ioctl for device" ]]; then
          echo ">> Unexpected error found in $err_file."
          wrong_files+=("$err_file")
          break
      fi
  done < "$err_file"
done

if [ ${#wrong_files[@]} -gt 0 ]; then
    echo ">> Errors were found in the following files:"
    for file in "${wrong_files[@]}"; do
        echo "      $file"
    done
    echo ">> Aborting script."
    exit 1
else
    echo "No unexpected error found. Good job!"
fi

# Creating .csv files

mkdir /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/data_$proc
source /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/createCsv.sh $proc data_$proc
rm /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/run_out_$proc_*
rm /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/file_out_$proc_*
rm /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/condor_out_$proc_*

# Moving results to outDir

mkdir /afs/cern.ch/user/c/ccarriva/ZZHH/Output/$proc
mkdir /afs/cern.ch/user/c/ccarriva/ZZHH/Output/$proc/xsec
mv /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/data_$proc /afs/cern.ch/user/c/ccarriva/ZZHH/Output/$proc/xsec
mv /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/out_$proc/Events/ /afs/cern.ch/user/c/ccarriva/ZZHH/Output/$proc/xsec

# Nocuts plots
(
cd /afs/cern.ch/user/c/ccarriva/ZZHH/CMSSW_13_0_16/src
cmsenv
cd -
python3 /afs/cern.ch/user/c/ccarriva/ZZHH/scripts/my_analyzer_cuts.py $proc $proc m1100
)
exit 0
