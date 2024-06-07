#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

for oppe in FS0 FS1 FS2 FM0 FM1 FM2 FM3 FM4 FM5 FM7
  do

  cp ${2}/model_all.csv ${2}/model_Eboli_${1}_${oppe}.csv
  more run_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -1 | sed "s#     Cross-section :   #0.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}.csv
  more run_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -2 | tail -1 | sed "s#     Cross-section :   #-20.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}.csv
  more run_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -3 | tail -1 | sed "s#     Cross-section :   #-10.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}.csv
  more run_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -4 | tail -1 | sed "s#     Cross-section :   #-5.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}.csv
  more run_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -5 | tail -1 | sed "s#     Cross-section :   #-2.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}.csv
  more run_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -6 | tail -1 | sed "s#     Cross-section :   #2.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}.csv
  more run_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -7 | tail -1 | sed "s#     Cross-section :   #5.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}.csv
  more run_${1}_${oppe}_cuts.out | grep "Cross-sect" | head -8 | tail -1 | sed "s#     Cross-section :   #10.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}.csv
  more run_${1}_${oppe}_cuts.out | grep "Cross-sect" | tail -1 | sed "s#     Cross-section :   #20.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}.csv
done

#for oppe in FS0 FS1 FS2 FM0 FM1 FM2 FM3 FM4 FM5 FM7
#  do

#  cp ${2}/model_all.csv ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#  more ../run_${1}_${oppe}_unirest.out.old | grep "Cross-sect" | head -1 | sed "s#     Cross-section :   #0.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#  more ../run_${1}_${oppe}_unirest.out.old | grep "Cross-sect" | head -2 | tail -1 | sed "s#     Cross-section :   #-20.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#  more ../run_${1}_${oppe}_unirest.out.old | grep "Cross-sect" | head -3 | tail -1 | sed "s#     Cross-section :   #-10.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#  more ../run_${1}_${oppe}_unirest.out.old | grep "Cross-sect" | head -4 | tail -1 | sed "s#     Cross-section :   #-5.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#  more ../run_${1}_${oppe}_unirest.out.old | grep "Cross-sect" | head -5 | tail -1 | sed "s#     Cross-section :   #-2.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#  more ../run_${1}_${oppe}_unirest.out.old | grep "Cross-sect" | head -6 | tail -1 | sed "s#     Cross-section :   #2.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#  more ../run_${1}_${oppe}_unirest.out.old | grep "Cross-sect" | head -7 | tail -1 | sed "s#     Cross-section :   #5.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#  more ../run_${1}_${oppe}_unirest.out.old | grep "Cross-sect" | head -8 | tail -1 | sed "s#     Cross-section :   #10.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#  more ../run_${1}_${oppe}_unirest.out.old | grep "Cross-sect" | tail -1 | sed "s#     Cross-section :   #20.,#g" | sed "s# +- #,#g" | sed "s#pb##g" >> ${2}/model_Eboli_${1}_${oppe}_unitarity.csv
#done
