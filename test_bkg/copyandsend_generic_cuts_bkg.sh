#!/bin/bash
                                                                                
fail_exit() { echo "$@" 1>&2; exit 1; }                                         
                                                                                
echo "Start of job on " `date`                                                  
                                                                                
cd /afs/cern.ch/user/a/acappati/work/ZZH/220303_process4/CMSSW_11_2_3           
eval `scram runtime -sh`                                                        
cd /afs/cern.ch/user/a/acappati/work/ZZH/220303_process4/MG5_aMC_v2_7_3_py3     
                                                                                
cp ../ZZH/dummy_fct_ppTozbbbb.f ${1}/SubProcesses/dummy_fct.f                   
python bin/mg5_aMC file_${1}.txt
