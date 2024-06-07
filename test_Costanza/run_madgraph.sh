#!/bin/bash

file="processes.csv"

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
  echo "No matching process found for $1"
  exit 1
fi

rm -r out_$proc
cmd_file="mg5_cmd.txt"

  echo "n" > $cmd_file
  echo "import model SM_Ltotal_Ind5v2020v2_UFO" >> $cmd_file
  echo $mg5_string >> $cmd_file
  echo "output out_$proc" >> $cmd_file
  echo "quit" >> $cmd_file

python3 bin/mg5_aMC $cmd_file > mg5_$proc.log

rm $cmd_file
cp ../../ZZH/dummy_fct_forWZ.f out_$proc/SubProcesses/dummy_fct.f
exit 0
