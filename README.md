# ZZHH

Framework for extraction of limits on EFT parameters including unitarity constraints. Setup for lxplus9.
Clone the repository and run the configuration script:

```bash
git clone https://github.com/ZZHHmultiboson/ZZHH.git
./config_lp9.sh
```

Define your process in processes.csv using the following syntax:

```bash
$PROC_NAME,$MG5_SYNTAX
```
e.g.

```bash
wpzh,generate p p > w+ z h QED=3
```
To produce cross section for different values of involved dim8 operators (FS0, FS1, FS2, FM1, FM2, FM3, FM4, FM5, FM7), run the command:

```bash
./run_madgraph.sh $PROC_NAME
```
Cross section results, as well as plots of cross section VS FSi, are stored in Output/$PROC_NAME directory.