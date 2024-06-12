#!/bin/bash

# Searching for process definition

file="../backgrounds.csv"

proc=""
mg5_string=""

while IFS=, read -r name string; do
  if [[ $name == $1 ]]; then
    proc=$name
    mg5_string=$string
    break
  fi
done < $file

if [[ -z $proc ]]; then
  echo "No matching background found for $1"
  exit 1
fi

# Launching MadGraph

rm -r out_$proc
cmd_file="mg5_cmd.txt"

  echo "n" > $cmd_file
  echo $mg5_string >> $cmd_file
  echo "output out_$proc" >> $cmd_file
  echo "quit" >> $cmd_file

python3 bin/mg5_aMC $cmd_file > mg5_$proc.log

rm $cmd_file
cp ../scripts/dummy_fct_ppTozbbbb.f out_$proc/SubProcesses/dummy_fct.f

# Launching job for Cross Section on condor

source sendOne_cuts.sh out_$proc
log_file="run_out_${proc}_${operator}.log"
err_file="run_out_${proc}_${operator}_cuts.err"
condor_wait $log_file

# Checking if all jobs ended correctly

declare -a wrong_files
while IFS= read -r line; do
    if [[ ! $line =~ ^[[:space:]]*0% && ! $line =~ ^[[:space:]]*100% && ! $line == "stty: 'standard input': Inappropriate ioctl for device" ]]; then
        echo ">> Unexpected error found in $err_file."
        wrong_files+=("$err_file")
        break
    fi
done < "$err_file"

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

mkdir data_$proc
source createCsv.sh $proc data_$proc
rm run_out_$proc_*
rm file_out_$proc_*
rm condor_out_$proc_*

# Moving results to outDir

mkdir ../Output/$proc
mkdir ../Output/$proc/xsec
mv data_$proc ../Output/$proc/xsec
mv out_$proc/Events/ ../Output/$proc/xsec

exit 0
