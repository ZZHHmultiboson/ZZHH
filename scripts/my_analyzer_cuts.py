#! /usr/bin/env python3

import sys
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#mpl.use('agg') #ignora plt.show
import seaborn as sns
sns.set(context='notebook', style='whitegrid', font_scale=1.3) #cambia tema dei plot (la size 1.3 dovrebbe corrispondere a font 16 in mpl)
import os
import numpy as np
from scipy.optimize import curve_fit
import json
#import pprintpp
from cycler import cycler



def func(x,a,b,c):
    return a*x**2+b*x+c 


def main():

    if (len(sys.argv) < 2): 
        print("specify the process, please")
        sys.exit(1)

    # --- out directory
    processo = sys.argv[1]
    processo2 = sys.argv[2]
    cuts = ""
    if (len(sys.argv) > 3): 
        cuts = sys.argv[3]

    out_dir = 'plots_' + processo + '_' + cuts
    os.makedirs(out_dir,exist_ok=True) #check if output dir exist

    # --- dictionary for results
    fit_results = {}

    # --- input file names
    name_list = ['FS0','FS1','FS2','FM0','FM1','FM2','FM3','FM4','FM5','FM7']
    #if ("wz" in processo):
    #    name_list = ['FS0','FS1','FS2','FM0','FM1','FM2','FM3','FM4','FM5','FM6']
    #name_list = ['FS2']
    #name_list = ['FS0','FS1','FS2','FM1']


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
    
    # read input file
    for i_name in name_list:
        csv = 'data_' + processo + "/model_Eboli_" + processo2 + "_" + i_name + '.csv' 
        cols = ['operator', 'crossSection', 'crossSectionErr']
        df = pd.read_csv(csv, comment='#', sep=',',names=cols)
        #df = pd.read_csv(csv, comment='#', sep=',')
        
        x_arr    = df['operator'].values
        y_arr_orig    = 1000.*df['crossSection'].values
        yerr_arr_orig = 1000.*df['crossSectionErr'].values
        y_arr = np.multiply(y_arr_orig,br)
        yerr_arr = np.multiply(yerr_arr_orig,br)
        df['crossSection'] = y_arr
        df['crossSectionErr'] = yerr_arr

        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,5)) #crea griglia di plots
        #sns.scatterplot(data=df, x='operator', y='crossSection',color='g',ax=ax)
        # --- plot with error bars
        plt.errorbar(data=df,
                     x='operator',
                     y='crossSection',
                     yerr='crossSectionErr',
                     marker='.',
                     markersize='7',
                     linestyle='',
                     color='black',
                    )
        
        # --- do the fit
        params, covs = curve_fit(func,
                                 xdata=x_arr,
                                 ydata=y_arr,
                                 sigma=yerr_arr,
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
        x = np.linspace(np.min(df['operator']),
                        np.max(df['operator']),
                        num=1000
                       )
        
        sns.lineplot(x=x,
                     y=func(x,params[0],params[1],params[2]),
                     color='red',
                     linestyle='-',
                     ax=ax
                    )
        
        
        ax.set_xlabel('$operator/\Lambda^4 [TeV^{-4}]$')
        ax.set_ylabel('$\overline{\sigma}$ (1.1, 13 TeV) [fb]')
        #ax.legend(['FS0'],loc='best') #legenda nel best place
        ax.legend([ i_name +' fit', i_name ],loc='upper left', bbox_to_anchor=(1.0, 1.0)) #legenda dove dico io
        #x_ticks = np.linspace(np.floor(np.min(df['operator'])),np.ceil(np.max(df['operator'])),num=10) #crea num tick tra i due estremi
        #ax.set_xticks(x_ticks)
        
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, i_name +'.png'), dpi=300) #save plot, resolution
        plt.savefig(os.path.join(out_dir, i_name +'.pdf'), dpi=300) #save plot, resolution
#        plt.show() #mi mostra la finestra del plot, da togliere se usi nelle code
        plt.close(fig) #libera memoria da fig


    # --- save file with fit results
    with open(os.path.join(out_dir, 'fitResults.json'),'w') as f:
        json.dump(fit_results,f)

    #pprintpp.pprint(fit_results) #print nicely the dictionary
 

    
    # --- plot curves all together
    fig_all, ax_all = plt.subplots(nrows=1, ncols=1, figsize=(8,5))
        
    x_all = np.linspace(-50.,
                        50.,
                        num=1000
                       )

    num_color = len(fit_results.keys())
    color_list  = sns.color_palette('hls',num_color)
    legend_list = ['$f_{S0}$','$f_{S1}$','$f_{S2}$','$f_{M0}$','$f_{M1}$','$f_{M2}$','$f_{M3}$','$f_{M4}$','$f_{M5}$','$f_{M7}$']
    
    for idk, key in enumerate(fit_results.keys()):

        sns.lineplot(x=x_all,
                     y=func(x_all,fit_results[key]['a'],fit_results[key]['b'],fit_results[key]['c']),
                     color=color_list[idk],
                     linestyle='-',
                     ax=ax_all,
                     label=legend_list[idk]
                    )
        print(key)
        print(legend_list[idk])

    ax_all.set_xlabel('$f_{i}/\Lambda^4 [TeV^{-4}]$')
    ax_all.set_ylabel('$\overline{\sigma}$ (1.1, 13 TeV) [fb]')
    #ax_all.legend(legend_list) #,loc='upper left', bbox_to_anchor=(1.0, 1.0)
    ax_all.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'allOperators.png'), dpi=300)
    plt.savefig(os.path.join(out_dir, 'allOperators.pdf'), dpi=300)

    # --- save zoom version
    ax_all.set_xlim(-10.,10.)
    ax_all.set_ylim(-1.,20.)   # hh
    if ("wpwp" in processo2): 
        ax_all.set_ylim(-0.1,2.)   # ww os
    if ("wpmz" in processo2): 
        ax_all.set_ylim(3.,5.5)   # wz
    if ("wpwm" in processo2): 
        ax_all.set_ylim(-1.,7.5)   # ww ss
    plt.savefig(os.path.join(out_dir, 'allOperators_zoom.png'), dpi=300)

    plt.close(fig_all)
    
        

if __name__=="__main__":
    main()
    exit(0)
