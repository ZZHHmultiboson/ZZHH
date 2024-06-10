#!/bin/bash

# Searching for process definition

file="processes.csv"

proc=""
mg5_string=""

while IFS=, read -r name string br; do
  if [[ $name == $1 ]]; then
    proc=$name
    mg5_string=$string
    break
  fi
done < $file

if [[ -z $proc ]]; then
  echo "No matching process found for $1"
  exit 1
fi

# Launching MadGraph

rm -r MG5_aMC_v2_9_18/out_$proc
cmd_file="MG5_aMC_v2_9_18/mg5_cmd.txt"

  echo "n" > $cmd_file
  echo "convert model /afs/cern.ch/user/c/ccarriva/ZZHH/MG5_aMC_v2_9_18/models/SM_Ltotal_Ind5v2020v2_UFO" > $cmd_file
  echo "import model SM_Ltotal_Ind5v2020v2_UFO" >> $cmd_file
  echo $mg5_string >> $cmd_file
  echo "output out_$proc" >> $cmd_file
  echo "quit" >> $cmd_file

python3 MG5_aMC_v2_9_18/bin/mg5_aMC $cmd_file > mg5_$proc.log

rm $cmd_file
cp scripts/dummy_fct_forWZ.f out_$proc/SubProcesses/dummy_fct.f

# Launching jobs for Cross Section on condor

operators=("FS0" "FS1" "FS2" "FM0" "FM1" "FM2" "FM3" "FM4" "FM5" "FM7")
log_files=()
err_files=()
for operator in "${operators[@]}"; do
  source MG5_aMC_v2_9_18/sendOne_cuts.sh out_$proc $operator
  log_files+=("MG5_aMC_v2_9_18/run_out_${proc}_${operator}.log")
  err_files+=("MG5_aMC_v2_9_18/run_out_${proc}_${operator}_cuts.err")
done

for log_file in "${log_files[@]}"; do
  condor_wait $log_file
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

mkdir MG5_aMC_v2_9_18/data_$proc
source MG5_aMC_v2_9_18/createCsv.sh $proc data_$proc
rm MG5_aMC_v2_9_18/run_out_$proc_*
rm MG5_aMC_v2_9_18/file_out_$proc_*
rm MG5_aMC_v2_9_18/condor_out_$proc_*

# Moving results to outDir

mkdir Output/$proc
mkdir Output/$proc/xsec
mv MG5_aMC_v2_9_18/data_$proc Output/$proc/xsec
mv MG5_aMC_v2_9_18/out_$proc/Events/ Output/$proc/xsec

# Nocuts plots

cd CMSSW_13_0_16/src
cmsenv
cd -
python3 MG5_aMC_v2_9_18/my_analyzer_cuts.py $proc $proc m1100

exit 0
