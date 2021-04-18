import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
from tabulate import tabulate

def LossRecovery(decrease):
    inv = 100
    loss_percentage = 0
    np_array_lp = np.array([])
    np_array_lp_f = np.array([])
    gain_to_initial = 0 
    np_array_gti = np.array([])
    np_array_gti_f = np.array([])
    np_array_dif = np.array([])
    for i in range(1,decrease):
        loss_percentage = (i / inv)
        np_array_lp = np.append(np_array_lp,loss_percentage)
        np_array_lp_f = np.append(np_array_lp_f,"{:.2%}".format(loss_percentage))
        gain_to_initial = (i / (inv - i))
        np_array_gti = np.append(np_array_gti,gain_to_initial)
        np_array_gti_f = np.append(np_array_gti_f,"{:.5%}".format(gain_to_initial))
        np_array_dif = np.append(np_array_dif,"{:.5%}".format(gain_to_initial - loss_percentage))
    #Graph_1
    plt.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.subplot(1,2,1)
    plt.grid(color='#2A3459')  # bluish dark grey, but slightly lighter than background
    plt.plot(np_array_lp, np_array_gti,marker='o',color='#08F7FE')
    n_lines = 10
    diff_linewidth = 1.05
    alpha_value = 0.03
    for n in range(1, n_lines+1):
        plt.plot(np_array_lp, np_array_gti,marker='o',linewidth=2+(diff_linewidth*n),alpha=alpha_value,color='#08F7FE')
    plt.xlabel("Loss Percentage")
    plt.ylabel("Return to Initial Investment")
    plt.autoscale()
    #Graph_2
    plt.subplot(1,2,2)
    plt.grid(color='#2A3459')  # bluish dark grey, but slightly lighter than background
    plt.plot(np_array_lp, np_array_gti-np_array_lp,marker='o',color='#08F7FE')
    for n in range(1, n_lines+1):
        plt.plot(np_array_lp, np_array_gti-np_array_lp,marker='o',linewidth=2+(diff_linewidth*n),alpha=alpha_value,color='#08F7FE')
    plt.xlabel("Loss Percentage")
    plt.ylabel("Return to Initial Investment - Loss Percentage")
    plt.autoscale()
    plt.show()

    df = pd.DataFrame({'Loss':np_array_lp_f, 'Return to Initial Investment':np_array_gti_f, 'Diference':(np_array_dif)})
    print(tabulate(df, headers='keys', tablefmt='psql'))

LossRecovery(30)





