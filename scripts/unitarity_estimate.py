#! /usr/bin/env python3

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#mpl.use('agg') #ignora plt.show
import seaborn as sns
#sns.set_theme(context='notebook',style='whitegrid') #cambia tema dei plot
sns.set(context='notebook',style='whitegrid', font_scale=1.3) #cambia tema dei plot (la size 1.3 dovrebbe corrispondere a font 16 in mpl)
import os
import numpy as np
from scipy.optimize import curve_fit
import json
#import pprintpp
from cycler import cycler
import math
import sys

def func(x,a,b,c):
    return a*x**2+b*x+c 

def vertexx(a,b,c):
    return -b/(2.*a)

def vertexy(a,b,c):
    return -(b**2-4.*a*c)/(4.*a)

def inversefuncplus(y,a,b,c):
    if (b**2-4.*a*(c-y)) > 0 : 
        return (-b+math.sqrt(b**2-4.*a*(c-y)))/(2.*a) 
    return 1000.

def inversefuncminus(y,a,b,c):
    if (b**2-4.*a*(c-y)) > 0 : 
        return (-b-math.sqrt(b**2-4.*a*(c-y)))/(2.*a) 
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

    # --- input file names
    '''
    oppe = 'FM0'
    limit_value_plus = 7.6   #assum: limit_value_minus = -limit_value_plus
    #limit_value_plus = 5.7    #assum: limit_value_minus = -limit_value_plus
    #limit_value_plus = 5.8   #assum: limit_value_minus = -limit_value_plus
    #lumiscale = math.sqrt(140./3000.)
    lumiscale = 1.

    cuts_list = ['1000000','1200','1400','1600','1800','2000','2500','3000','3500','4000','5000']
    name_list = ['FS0','FS1','FS2','FM0','FM1','FM2','FM3','FM4','FM5','FM7']
    '''
    cuts_list = ['1000000','1200','1400','1600','1800','2000','2500','3000','3500','4000','5000']
#    name_list = ['FS0', 'FS1', 'FS2', 'FM0', 'FM1', 'FM2', 'FM3', 'FM4', 'FM5', 'FM7']
    name_list = ['FS0', 'FS1', 'FS2', 'FM1', 'FM2', 'FM3', 'FM4', 'FM5', 'FM7']
    limit_values = [4.2, 5.2, 0.0, 1.0, 3.0, 1.8, 3.3, 3.6, 5.1] #best limits from WV semilep (arXiv:1905.07445) and Wgamma (arXiv:2212.12592)
    process = sys.argv[1]
    cutss = sys.argv[2]
    oppe = sys.argv[3]

    if oppe not in name_list:
        print(f"{oppe} is not a valid operator.")
        sys.exit(1)
    if oppe == 'FS2':
        print("No experimental limit found for FS2")
        sys.exit(1)
    
    index = name_list.index(oppe)
    limit_value_plus = limit_values[index]

    lumiscale = 1.

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
    xpoints = [1200.,1400.,1600.,1800.,2000.,2500.,3000.,3500.,4000.,5000.]
    ypoints = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
    ypointsminus = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
    cross95resc = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

    # fit parameters for all data (nocut)

    #f_nocut = open('plots_perUnitarity_wpzh_mWZH1100/fitResults_1000000.json',)
    f_nocut = open(f'../Output/{process}/plots_perUnitarity_{process}_{cutss}/fitResults_1000000.json')

    data_nocut = json.load(f_nocut)

    anocut = data_nocut[oppe]['a']
    bnocut = data_nocut[oppe]['b']
    cnocut = data_nocut[oppe]['c']
    i = -1

    with open(f'../Output/{process}/results_{process}.txt', 'w') as fi: # ouput file 
        for c_name in cuts_list:

            # fit parameters for each cut
            
            f = open(f'../Output/{process}/plots_perUnitarity_{process}_{cutss}/fitResults_'+c_name+'.json',)
            
            data = json.load(f)
            
            aor = data[oppe]['a']
            bor = data[oppe]['b']
            cor = data[oppe]['c']
            
            print (aor," ",bor," ",cor)
            
            cross95 = func(limit_value_plus,anocut,bnocut,cnocut)						# upper limit xsec
            distance_to_min = (cross95 - vertexy(anocut,bnocut,cnocut))/vertexy(anocut,bnocut,cnocut)		# max relative variation of xsec wrt sm
            print ("Excluded xsec no cut = ",cross95," Relative xsec 95% interval = ",distance_to_min)
            
            # now rescale for statistics!
            json_file = '../Output/'+ process + 'plotsAndFractions_wpzh/fractions_wpzh_'+oppe+'_0.json'
            ffrac = open(json_file)
            fractions = json.load(ffrac)
            newc_name = c_name+'.0'
            error_scale = 1./math.sqrt(float(fractions[newc_name])/float(fractions['1000000.0']))
            distance_to_min *= error_scale*lumiscale
            cross95resc[i+1] = vertexy(aor,bor,cor)*(1+distance_to_min)
            print ("Excluded xsec = ",cross95resc[i+1]," Relative xsec 95% interval rescaled = ",distance_to_min)
            
            limit_est_plus =  inversefuncplus(cross95resc[i+1],aor,bor,cor)
            limit_est_minus = inversefuncminus(cross95resc[i+1],aor,bor,cor)
            print (oppe," estimated limit with cutoff at ",c_name, " GeV : [",limit_est_minus,",",limit_est_plus,"]")
            if (c_name=='1000000'):
                print (oppe," estimated best limit with no unitarity : [",limit_est_minus,",",limit_est_plus,"]", file=fi)
            if i>-1:
                ypoints[i] = limit_est_plus
                ypointsminus[i] = limit_est_minus
            i += 1

        fig_all, ax_all = plt.subplots(nrows=1, ncols=1, figsize=(8,6))
        print (xpoints)
        print (ypoints)
        ax_all.plot(xpoints, ypoints, color='b', linestyle='-', label='CMS limits')
        ax_all.plot(xpoints, ypointsminus, color='b', linestyle='-')
        best_limit_plus = find_interseccion(xpoints,ypoints,data_coeff[oppe])
        best_limit_minus = find_interseccion(xpoints,ypointsminus,-data_coeff[oppe])
        
        print ("**********")
        print (oppe," estimated best limit with unitarity : [",best_limit_minus,",",best_limit_plus,"]")
        print (oppe," estimated best limit with unitarity : [",best_limit_minus,",",best_limit_plus,"]",file=fi)
        print ("**********")

        x = np.linspace(np.min(xpoints),
                        np.max(xpoints),
                        num=1000
                    )
        
        # PLOT ROSSO
        y = data_coeff[oppe]*(1000./x)**4
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
    
        ylabel = '$f_{'+oppe[1:3]+'}/\Lambda^4$ limit [TeV$^{-4}$]'
        ax_all.set_ylabel(ylabel)
        ax_all.set_xlabel('upper $m_{WZ}$ cut-off [GeV]')
        ax_all.set_xlim(np.min([np.min(x),np.min(xpoints)]), np.max([np.max(x),np.max(xpoints)])) # x axis limits
        ax_all.set_ylim(np.min([np.min(-y),np.min(ypointsminus)]), np.max([np.max(y),np.max(ypoints)])) # y axis limits
        ax_all.legend() #legenda nel best place
        #ax.legend([ i_name +' fit', i_name ],loc='upper left', bbox_to_anchor=(1.0, 1.0)) #legenda dove dico io
        #x_ticks = np.linspace(np.floor(np.min(df['operator'])),np.ceil(np.max(df['operator'])),num=10) #crea num tick tra i due estremi
        #ax.set_xticks(x_ticks)
    
        plt.tight_layout()
        plt.savefig('unitarityPlot_vbswz_'+oppe+'.pdf', dpi=300) #save plot, resolution
        #        plt.show() #mi mostra la finestra del plot, da togliere se usi nelle code
        plt.close(fig_all) #libera memoria da fig
        
        for i_name in name_list:
            i = -1
            if i_name == oppe:
                continue
            else:
                for c_name in cuts_list:
                    f = open('plots_perUnitarity_wpzh_mWZH1100/fitResults_'+c_name+'.json',)
                    data = json.load(f)
                    
                    aa = data[i_name]['a']
                    bb = data[i_name]['b']
                    cc = data[i_name]['c']
                    print (aa," ",bb," ",cc)
                    #this_cross95 = cross95 - vertexy(aor,bor,cor) + vertexy(aa,bb,cc) 
                    limit_est_plus =  inversefuncplus(cross95resc[i+1],aa,bb,cc)
                    limit_est_minus = inversefuncminus(cross95resc[i+1],aa,bb,cc)
                    print (i_name," estimated limit with cutoff at ",c_name, " GeV : [",limit_est_minus,",",limit_est_plus,"]")
                    if (c_name=='1000000'):
                        print (i_name," estimated best limit with no unitarity : [",limit_est_minus,",",limit_est_plus,"]", file=fi)
                    if i>-1:
                        ypoints[i] = limit_est_plus
                        ypointsminus[i] = limit_est_minus
                    i += 1  

                fig_all, ax_all = plt.subplots(nrows=1, ncols=1, figsize=(8,6))
                # print (xpoints)
                # print (ypoints)
                ax_all.plot(xpoints, ypoints, color='b', linestyle='-', label='CMS limits')
                ax_all.plot(xpoints, ypointsminus, color='b', linestyle='-')
                best_limit_plus = find_interseccion(xpoints,ypoints,data_coeff[i_name])
                best_limit_minus = find_interseccion(xpoints,ypointsminus,-data_coeff[i_name])
                
                print ("**********")
                print (i_name," estimated best limit with unitarity : [",best_limit_minus,",",best_limit_plus,"]")
                print (i_name," estimated best limit with unitarity : [",best_limit_minus,",",best_limit_plus,"]",file=fi)
                print ("**********")
            
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
                               
                ylabel = '$f_{'+i_name[1:3]+'}/\Lambda^4$ limit [TeV$^{-4}$]'
                ax_all.set_ylabel(ylabel)
                ax_all.set_xlabel('upper $m_{WZ}$ cut-off [GeV]')
                ax_all.set_xlim(np.min([np.min(x),np.min(xpoints)]), np.max([np.max(x),np.max(xpoints)])) # x axis limits
                ax_all.set_ylim(np.min([np.min(-y),np.min(ypointsminus)]), np.max([np.max(y),np.max(ypoints)])) # y axis limits
                ax_all.legend() #legenda nel best place
                #ax.legend([ i_name +' fit', i_name ],loc='upper left', bbox_to_anchor=(1.0, 1.0)) #legenda dove dico io
                #x_ticks = np.linspace(np.floor(np.min(df['operator'])),np.ceil(np.max(df['operator'])),num=10) #crea num tick tra i due estremi
                #ax.set_xticks(x_ticks)
                
                plt.tight_layout()
                plt.savefig('unitarityPlot_wpzh_'+i_name+'.pdf', dpi=300) #save plot, resolution
                #        plt.show() #mi mostra la finestra del plot, da togliere se usi nelle code
                plt.close(fig_all) #libera memoria da fig        
                
  

if __name__=="__main__":
    main()
    exit(0)
