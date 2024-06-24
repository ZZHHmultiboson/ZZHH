#! /usr/bin/env python3

import sys
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#mpl.use('agg') #ignora plt.show
import seaborn as sns
sns.set(context='notebook',style='whitegrid', font_scale=1.3) #cambia tema dei plot
import os
import numpy as np
from scipy.optimize import curve_fit
import json
#import pprintpp
from cycler import cycler
import math


def func(x,a,b,c):
    return a*x**2+b*x+c 


def main():

    # --- out directory
    processo = sys.argv[1]
    cuts = ""
    if (len(sys.argv) > 1): 
        cuts = sys.argv[2]
    print (processo)
    print (cuts)

    out_dir = '/afs/cern.ch/user/c/ccarriva/ZZHH//Output/' + processo + '/plots_perUnitarity_' + processo + '_' + cuts
    os.makedirs(out_dir,exist_ok=True) #check if output dir exist

    # --- dictionary for results
    fit_results = {}

    # --- input file names
    with open('operators.json', 'r') as file:
    	operators = json.load(file)
    	name_list = [key for key, value in operators.items() if value["turn"] == "on"]
    cuts_list = ['1000000.0','1200.0','1400.0','1600.0','1800.0','2000.0','2500.0','3000.0','3500.0','4000.0','5000.0']
    
    ## BRANCHING RATIO
    # --- vbf HH process
    # br = 0.3249   # hh -> 4b
    # if ("wpwm" in processo2): 
    #     br = 0.0494    # leptonic
    # if ("wpwp" in processo2): 
    #     br = 0.0494    # leptonic
    # if ("wpmz" in processo2): 
    #     br = 0.0148    # leptioic


    br_H = 5.824e-01  # h->bb (H125, YR4)
    br_Z = 3.3658e-02 # z->ll (e, mu, pdg)
    br_W = 10.86e-02 # w->lnu (e, mu, pdg)
    '''
    # --- gg->zzh and pp->zzh processes
    # --- 4 accounts for Z decay in e or mu, and combinatory for the 2 Z
    # br = br_H * br_Z * br_Z * 4.

    # --- pp->wzh process
    # --- 4 accounts for Z decay in e or mu, and W decay in e or mu
    br = br_H * br_Z * br_W * 4. 

    # --- pp->zhh process
    # --- 2 accounts for combinatory for the 2 H
    # br = br_H * br_H * br_Z * 2.

    # --- pp->zhjj process
    # br = br_H * br_Z * 2.
    '''
    
    # Read automatically the Branching Ratio

    key = sys.argv[1]
    #process_file = '/afs/cern.ch/user/c/ccarriva/ZZHH/processes.json'
    #with open(process_file, 'r') as file:
    #    data = json.load(file)
    #br_expression = data[key]["BR"]
    #br = eval(br_expression)

    #print(f"Branching Ratio = {br}")

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
    print(f"Branching Ratio = {br}")

    for c_name in cuts_list:
    
        for i_name in name_list:

            print("now doing ",i_name," with cut at ",c_name," GeV")

            csv = '/afs/cern.ch/user/c/ccarriva/ZZHH/Output/' + processo + '/xsec/data_' + processo + "/model_Eboli_" + processo + "_" + i_name + '.csv' 
            cols = ['operator', 'crossSection', 'crossSectionErr']
            df = pd.read_csv(csv, comment='#', sep=',',names=cols)
            dfcopy = df.copy()
            print(df.columns)
        
            x_arr         = df['operator'].values
            y_arr_orig    = 1000.*df['crossSection'].values
            yerr_arr_orig = 1000.*df['crossSectionErr'].values
            y_arr = np.multiply(y_arr_orig,br)
            yerr_arr = np.multiply(yerr_arr_orig,br)
            dfcopy['crossSection'] = y_arr
            dfcopy['crossSectionErr'] = yerr_arr
            opval = 0
            y_arr_partial = y_arr.copy()
            yerr_arr_partial = yerr_arr.copy()
        
            while opval < len(x_arr):
                json_name = str(int(abs(x_arr[opval])))
                if (x_arr[opval] < 0.):
                    json_name = "minus"+json_name
                json_file = '/afs/cern.ch/user/c/ccarriva/ZZHH/Output/' + processo + '/plotsAndFractions_' + processo + '/fractions_' + processo + '_'+i_name+'_'+json_name+'.json'
                ffrac = open(json_file)
                fractions = json.load(ffrac)
                fraction = float(fractions[c_name])/float(fractions['1000000.0'])
                y_arr_partial[opval] = y_arr[opval]*fraction
                yerr_arr_partial[opval] = math.sqrt((yerr_arr[opval]*fraction)**2 + (1./float(fractions[c_name]))**2)
                                                                    # trascurate total number of events
                dfcopy['crossSection'][opval] = y_arr_partial[opval]
                dfcopy['crossSectionErr'][opval] = yerr_arr_partial[opval]
                opval += 1 
      
            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,5)) #crea griglia di plots
            #sns.scatterplot(data=df, x='operator', y='crossSection',color='g',ax=ax)
            # --- plot with error bars
            plt.errorbar(data=dfcopy,
                         x='operator',
                         y='crossSection',
                         yerr='crossSectionErr',
                         marker='.',
                         markersize='7',
                         linestyle='',
                         color='black',
                     )
            
            # --- do the fit / normalized xsec 
            params, covs = curve_fit(func,
                                     xdata=x_arr,
                                     ydata=y_arr_partial,
                                     sigma=yerr_arr_partial,
                                     absolute_sigma=True
                                 )
            print(params)
            print(covs)

            # --- save fit results in dictionary
            fit_results[i_name] = {'a': params[0],
                                   'aerror': np.sqrt(covs[0][0]),
                                   'b': params[1],
                                   'berror': np.sqrt(covs[1][1]),
                                   'c': params[2],
                                   'cerror': np.sqrt(covs[2][2])
                               }
            
            # --- plot fit
            x = np.linspace(np.min(dfcopy['operator']),
                            np.max(dfcopy['operator']),
                            num=1000
                        )
            
            sns.lineplot(x=x,
                         y=func(x,params[0],params[1],params[2]),
                         color='red',
                         linestyle='-',
                         ax=ax
                     )

            xlabel = '$f_{'+i_name[1:3]+'}/\Lambda^4$ (TeV$^{-4}$)'
            ylabel = '$\sigma$ [1.1, '+c_name[0:1]+'.'+c_name[1:2]+' TeV] (fb)'
            if (c_name == "1000000.0"):
                ylabel = '$\sigma$ [1.1, 13 TeV] (fb)'
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            #ax.legend(['FS0'],loc='best') #legenda nel best place
            ax.legend([ '$f_{'+i_name[1:3]+ '}$ fit', '$f_{'+i_name[1:3]+ '}$ data' ],loc='upper left', bbox_to_anchor=(1.0, 1.0)) #legenda dove dico io
            #x_ticks = np.linspace(np.floor(np.min(df['operator'])),np.ceil(np.max(df['operator'])),num=10) #crea num tick tra i due estremi
            #ax.set_xticks(x_ticks)
           
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, i_name +'_'+c_name[0:-2]+'.png'), dpi=300) #save plot, resolution
            #        plt.show() #mi mostra la finestra del plot, da togliere se usi nelle code
            plt.close(fig) #libera memoria da fig


        # --- plot curves all together
        fig_all, ax_all = plt.subplots(nrows=1, ncols=1, figsize=(8,5))
        
        x_all = np.linspace(-50.,
                            50.,
                            num=1000
        )
            
        num_color = len(fit_results.keys())
        color_list  = sns.color_palette('hls',num_color)
        legend_list = []
        
        for idk, key in enumerate(fit_results.keys()):
            
            sns.lineplot(x=x_all,
                         y=func(x_all,fit_results[key]['a'],fit_results[key]['b'],fit_results[key]['c']),
                         color=color_list[idk],
                         linestyle='-',
                         ax=ax_all
            )
            legend_list.append(key)
            
        ax_all.set_xlabel('operator [TeV-4]')
        ax_all.set_ylabel('xsec [fb]')
        ax_all.legend(legend_list,loc='upper left', bbox_to_anchor=(1.0, 1.0))
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, 'allOperators_'+c_name[0:-2]+'.png'), dpi=300)

        plt.close(fig_all)
        
        # --- save file with fit results
        with open(os.path.join(out_dir, 'fitResults_'+c_name[0:-2]+'.json'),'w') as f:
            json.dump(fit_results,f)
            
        #pprintpp.pprint(fit_results) #print nicely the dictionary


if __name__=="__main__":
    main()
    exit(0)
