#! /usr/bin/env python3

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#mpl.use('agg') #ignora plt.show
import seaborn as sns
sns.set(context='notebook',style='whitegrid', font_scale=1.3) #cambia tema dei plot (la size 1.3 dovrebbe corrispondere a font 16 in mpl)
import os
import numpy as np
from scipy.optimize import curve_fit
import json
#import pprintpp
from cycler import cycler
import math
from ROOT import TFeldmanCousins
import sys


def func(x,a,b,c):
    return a*x**2+b*x+c 

def vertexx(a,b,c):
    return -b/(2.*a)

def vertexy(a,b,c):
    return -(b**2-4.*a*c)/(4.*a)

def inversefuncplus(y,a,b,c):
    if (b**2 - 4.*a*(c-y)) > 0 : 
        return (-b + np.sqrt(b**2 - 4.*a*(c-y)))/(2.*a) 
    return 1000.

def inversefuncminus(y,a,b,c):
    if (b**2 - 4.*a*(c-y)) > 0 : 
        return (-b - np.sqrt(b**2 - 4.*a*(c-y)))/(2.*a) 
    return -1000.

def find_interseccion(xpoints,ypoints,coeff):
    j = 0
    k = 0
    while (j<9):
        if ((ypoints[j]-coeff*(1000./xpoints[j])**4)*(ypoints[j+1]-coeff*(1000./xpoints[j+1])**4) < 0.) :
            xmin = xpoints[j]
            xmax = xpoints[j+1]
            ymin = ypoints[j]                                                                                                                                                                              
            ymax = ypoints[j+1]
            while (k < 15):
                xhalf = 0.5*(xmin+xmax)
                yhalf = 0.5*(ymin+ymax)
                if ((ymin-coeff*(1000./xmin)**4)*(yhalf-coeff*(1000./xhalf)**4) > 0.) :
                   xmin = xhalf
                   ymin = yhalf
                else :
                   xmax = xhalf
                   ymax = yhalf
                k += 1   
            return yhalf    
        j += 1
    return coeff*(1000./xpoints[0])**4

def main():

    # --- out directory
    process = sys.argv[1]
    cutss = sys.argv[2]
    outdir = '/afs/cern.ch/user/c/ccarriva/ZZHH/Output/'+process+'/unitarityPlots/'
    os.makedirs(outdir, exist_ok=True)
    # --- inputs
    lumi = 140. #Run2
    #lumi = 3000. #HL-LHC
    eff = 0.7 # efficiency: obtained from muon selection eff (98%) times ele selection eff (95%) times b jets sel eff (75% medium WP)
    acceptans_sig = 0.93 # acceptance value obtained from acceptance_ZHH_cfg.py
    acceptans_bkg = 0.71 # acceptance value obtained from acceptance_ZHH_cfg.py
    total_eff_sig = eff*acceptans_sig
    total_eff_bkg = eff*acceptans_bkg

    cuts_list = ['1000000','1200','1400','1600','1800','2000','2500','3000','3500','4000','5000']
    name_list = ['FS0','FS1','FS2','FM0','FM1','FM2','FM3','FM4','FM5','FM7']
    # coeff from Eboli paper
    data_coeff = {
        'FS0' : 100.531,
        'FS1' : 43.0847,
        'FS2' : 60.3186,
        'FM0' : 41.0416,
        'FM1' : 164.1664,
        'FM2' : 35.5431,
        'FM3' : 142.1723,
        'FM4' : 100.5310,
        'FM5' : 201.0619,
        'FM7' : 328.3328
    }

    processes_def = '/afs/cern.ch/user/c/ccarriva/ZZHH/processes.json'
    with open(processes_def, 'r') as file:
        data = json.load(file)
    background = data.get(process, {}).get('bkg')
    print("Background for this process:", background)

    xpoints = [1200.,1400.,1600.,1800.,2000.,2500.,3000.,3500.,4000.,5000.]
    ypoints = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
    ypointsminus = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
    cross95resc = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
    tf = TFeldmanCousins(0.95)
    tf.SetMuMax(20) # 20 per Run2 #500 per HL LHC
    tf.SetMuStep(0.0001) #0.0001 per Run2 #0.01 per HL LHC
    i = -1

    for c_name in cuts_list:
 
        newc_name = c_name+'.0'
                    
        # --- bkg file with fractions
        json_fileb = '/afs/cern.ch/user/c/ccarriva/ZZHH/Output/'+background+'/plotsAndFractions_'+background+'/fractions_'+background+'_SMbkg_0.json' # mbb cut [115, 135], 10 GeV resol 
        ffracb = open(json_fileb)
        fractionsb = json.load(ffracb)

        # signal fit results
        f = open('/afs/cern.ch/user/c/ccarriva/ZZHH/Output/'+process+'/plots_perUnitarity_'+process+'_'+cutss+'/fitResults_'+c_name+'.json',)
        print('Reading file fitResults_'+c_name+'.json ...')
        data = json.load(f)
        sm_signal = data['FM0']['c']*lumi*total_eff_sig
        #DEBUG
        #print('DEBUG ',data['FM0']['c'], data['FM1']['c'], data['FM2']['c'], data['FM3']['c'], data['FM4']['c'], data['FM5']['c'], data['FM7']['c'], data['FS0']['c'], data['FS1']['c'], data['FS2']['c'])

        # read csv file with bkg xsec
        csv = '/afs/cern.ch/user/c/ccarriva/ZZHH/Output/'+background+'/xsec/data_'+background+'/model_Eboli_'+background+'.csv' # mbb cut [115, 135], 10 GeV resol    

        df = pd.read_csv(csv, comment='#', sep=',')
        
        processes_file = '/afs/cern.ch/user/c/ccarriva/ZZHH/processes.json'
        decay_file = '/afs/cern.ch/user/c/ccarriva/ZZHH/decay.json'
        with open(processes_file, 'r') as file:
            processes_data = json.load(file)
        with open(decay_file, 'r') as file:
            decay_data = json.load(file)
        br_expression = processes_data.get(process, {}).get('BR')
        for key, value in decay_data.items():
            br_expression = br_expression.replace(key, str(value))
        br = eval(br_expression)

        sm_bkg_tot = 1000.*br*df['crossSection'].values # transform bkg xsec from pb in fb, and multiply for BR (2*Z->ll, e, mu)
        sm_bkg = sm_bkg_tot[0]*float(fractionsb[newc_name])/float(fractionsb['1000000.0'])*lumi*total_eff_bkg
        #print( "sig/bkg = ", sm_signal, sm_bkg)

        # compute upper limit
        lim95 = tf.CalculateUpperLimit(sm_bkg + sm_signal, sm_bkg)
        print( 'sm_bkg            ', sm_bkg)
        print( 'sm_signal         ', sm_signal)
        print( 'sm_bkg + sm_signal', sm_bkg + sm_signal)
        cross95resc[i+1] = lim95/(total_eff_sig*lumi)
        print( "Excluded xsec = ", cross95resc[i+1], " fb")
        i += 1
            
    ## do the plots
    for i_name in name_list:
        i = -1
        for c_name in cuts_list:
            f = open('/afs/cern.ch/user/c/ccarriva/ZZHH/Output/'+process+'plots_perUnitarity_'+process+'_'+cutss+'/fitResults_'+c_name+'.json',)
            data = json.load(f)
            
            aa = data[i_name]['a']
            bb = data[i_name]['b']
            cc = data[i_name]['c']
            #print( aa," ",bb," ",cc," ",cross95resc[i+1])
            #this_cross95 = cross95 - vertexy(aor,bor,cor) + vertexy(aa,bb,cc) 
            limit_est_plus =  inversefuncplus(cross95resc[i+1],aa,bb,cc)
            limit_est_minus = inversefuncminus(cross95resc[i+1],aa,bb,cc)
            print( i_name," estimated limit with cutoff at ",c_name, " GeV : [",limit_est_minus,",",limit_est_plus,"]")
           # if (c_name=='1000000'):
              #  print i_name," estimated best limit with no unitarity : [",limit_est_minus,",",limit_est_plus,"]", file=fi)
            if i>-1:
                ypoints[i] = limit_est_plus
                ypointsminus[i] = limit_est_minus
            i += 1  
                    
        fig_all, ax_all = plt.subplots(nrows=1, ncols=1, figsize=(8,6))
        # print (xpoints)
        # print (ypoints)

        # PLOT NERO (risultati Run2 per operatore FM5)
        if (i_name=='FM5' and lumi==3000.) :
            yoldminus = [-181.17374483050634, -104.95166647827912, -81.5697446197898, -60.80321809984538, -57.55178762048659, -38.65548826075938, -29.99858959935547, -25.037058861248287, -22.349973244944085, -19.46501793147594]
            yoldplus = [194.457344672884, 113.93734255048089, 88.50984795183528, 66.38878267029342, 61.93330364009026, 41.07009995797042, 31.70967890986247, 26.471855186196354, 23.372642901188236, 20.243661975689548]
            ax_all.plot(xpoints, yoldplus, color='k', linestyle='-', label='CMS limits Run2')
            ax_all.plot(xpoints, yoldminus, color='k', linestyle='-')
            print('add Run2 results for FM5')

        # PLOT BLU
        ax_all.plot(xpoints, ypoints, color='b', linestyle='-', label='CMS limits HL')
        ax_all.plot(xpoints, ypointsminus, color='b', linestyle='-')
        best_limit_plus = find_interseccion(xpoints,ypoints,data_coeff[i_name])
        best_limit_minus = find_interseccion(xpoints,ypointsminus,-data_coeff[i_name])
        
        print( "**********")
        print( i_name," estimated best limit with unitarity : [",best_limit_minus,",",best_limit_plus,"]")
        print( "**********")
        
        x = np.linspace(np.min(xpoints),
                        np.max(xpoints),
                        num=1000
        )
        
        # PLOT ROSSO
        y = data_coeff[i_name]*(1000./x)**4
        sns.lineplot(x=x,
                     y=y,
                     color='red',
                     linestyle='-',
                     ax=ax_all,
                     label='unitarity bounds'
        )
        sns.lineplot(x=x,
                     y=-y,
                     color='red',
                     linestyle='-',
                     ax=ax_all
        )

        # fill area rossa sopra
        ax_all.fill_between(x, y, np.full_like(x, np.max([np.max(y),np.max(ypoints)])), color='none', hatch='///', edgecolor='r')
        # fill area rossa sotto
        ax_all.fill_between(x, np.full_like(x, np.min([np.min(-y),np.min(ypointsminus)])), -y, color='none', hatch='///', edgecolor='r')
        # fill area blu sopra
        ax_all.fill_between(xpoints, ypoints, np.full_like(xpoints, np.max([np.max(y),np.max(ypoints)])), color='none', hatch='\\\\\\', edgecolor='b')
        # fill area blu sotto
        ax_all.fill_between(xpoints, np.full_like(xpoints, np.min([np.min(-y),np.min(ypointsminus)])), ypointsminus, color='none', hatch='\\\\\\', edgecolor='b')
        
        
        ax_all.set_ylabel('$f_{'+i_name[1:3]+'}/\Lambda^4$ limit [TeV$^{-4}$]')
        ax_all.set_xlabel('upper $m_{ZHH}$ cut-off [GeV]')
        #ax_all.set_xscale('log') # log scale of x axis
        ax_all.set_xlim(np.min([np.min(x),np.min(xpoints)]), np.max([np.max(x),np.max(xpoints)])) # x axis limits
        ax_all.set_ylim(np.min([np.min(-y),np.min(ypointsminus)]), np.max([np.max(y),np.max(ypoints)])) # y axis limits

        ax_all.legend()

        
        plt.tight_layout()
        plt.gcf().savefig(os.path.join(outdir, 'unitarityPlot_'+process+'_'+i_name+'.png'), dpi=300)
        plt.gcf().savefig(os.path.join(outdir, 'unitarityPlot_'+process+'_'+i_name+'.pdf'), dpi=300)
        plt.close(fig_all) #libera memoria da fig        
    
  

if __name__=="__main__":
    main()
    exit(0)
