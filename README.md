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
> Branching ratios for bosons decays are defined in my_analyzer_cuts.py:
> * br_H = 5.824e-01 [ h->bb (H125, YR4) ]  
> * br_Z = 3.3658e-02 [ z->ll (e, mu, pdg) ]  
> * br_W = 10.86e-02 [ w->lnu (e, mu, pdg) ]  

To produce cross section for different values of involved dim8 operators (FS0, FS1, FS2, FM1, FM2, FM3, FM4, FM5, FM7), call the GRID certificate and run the script:

```bash
voms-proxy-init -voms cms -rfc --valid 168:0
cd MG5_aMC_v2_9_18
./run_madgraph.sh $PROC_NAME
```
Cross section results, as well as plots of cross section as a function of Fi, are stored in Output/$PROC_NAME directory.

## EFT limits w/ unitarity bounds

Limits on EFT parameters are derived at the mass point given by the intersection of theoretical curve and the one obtained varying the mass interval for xsec extraction.  
To plot xsec as a function of Fi at each mass point, compare the two curves and derive the final limit, run:

```bash
cd ..
./run_unitarity.sh $PROC_NAME $CUTS $REF_OP
```

$CUTS is an indicative expression of the global cut considered (e.g. for m(W,Z,H)=1.1 TeV, it can be mWZH1100).  The script takes as input the experimental limit on a chosen operator to derive limits on other operators, so you have to specify it as third argument ($REF_OP).  
>Best experimental limits to date are considered:
>
>| Wilson Coefficient | Best Experimental Limit | Analysis                       |
>|--------------------|-------------------------|--------------------------------|
>| FS0                | [-4.2; 4.2]             | WV semilep (arXiv:1905.07445)  |
>| FS1                | [-5.2; 5.2]             | WV semilep (arXiv:1905.07445)  |
>| FS2                | -                       | -                              |
>| FM0                | [-1.0; 1.0]             | WV semilep (arXiv:1905.07445)  |
>| FM1                | [-3.0; 3.0]             | WV semilep (arXiv:1905.07445)  |
>| FM2                | [-1.8; 1.8]             | Wgamma (arXiv:2212.12592)      |
>| FM4                | [-3.3; 3.3]             | Wgamma (arXiv:2212.12592)      |
>| FM5                | [-3.4; 3.6]             | Wgamma (arXiv:2212.12592)      |
>| FM7                | [-5.1; 5.1]             | WV semilep (arXiv:1905.07445)  |
