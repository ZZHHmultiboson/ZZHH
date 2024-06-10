# ZZHH

> Framework for extraction of limits on EFT parameters including unitarity constraints. Setup for lxplus9.

Clone the repository and run the configuration script:

```bash
git clone https://github.com/ZZHHmultiboson/ZZHH.git
cd ZZHH/
./config_lp9.sh
```

## Process generation and xsec plots w/o unitarity

Define your process in processes.csv using the following syntax:

```bash
$PROC_NAME,$MG5_SYNTAX,$BRANCHING_RATIO
```
e.g.

```bash
wpzh,generate p p > w+ z h QED=3,br_H * br_Z * br_W * 4.
```
> Branching ratios are defined in my_analyzer_cuts.py:
> * br_H = 5.824e-01 [ h->bb (H125, YR4) ]  
> * br_Z = 3.3658e-02 [ z->ll (e, mu, pdg) ]  
> * br_W = 10.86e-02 [ w->lnu (e, mu, pdg) ]  

To produce cross section for different values of involved dim8 operators (FS0, FS1, FS2, FM1, FM2, FM3, FM4, FM5, FM7), call the GRID certificate and run the script:

```bash
voms-proxy-init -voms cms -rfc --valid 168:0
nohup ./run_madgraph.sh $PROC_NAME > $PROC_NAME.log 2>&1 &
```
Cross section results, as well as plots of cross section as a function of FSi, are stored in Output/$PROC_NAME directory.

## EFT limits w/ unitarity bounds

