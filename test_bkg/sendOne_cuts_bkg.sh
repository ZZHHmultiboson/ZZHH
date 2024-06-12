#!/bin/bash                                                                                                                                                                                                
fail_exit() { echo "$@" 1>&2; exit 1; }                                                             
                                                                                                                                                                                                           
echo "Start of job on " `date`                        
                                                                                                                                                                                                          
cat MG5config_generic_cuts.txt | sed "s#SIGNAL#${1}#g" > file_${1}.txt                           
cat condor_cuts.sub | sed "s#SIGNAL#${1}#g" > condor_${1}_cuts.sub                        
condor_submit condor_${1}_cuts.sub
