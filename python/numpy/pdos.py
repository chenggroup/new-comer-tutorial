#!/Users/jinyuanhu/anaconda3/bin/python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
def plot_pdos(x, y_1, y_2, y_3):
    y_max = 8
    y_min = -6
    x_max = 15
    x_min = -1 
    fig_x = 8 
    fig_y = 14
    lw = 2 
    fs = 24
    x_ticks = []
    y_ticks = np.arange(y_min, y_max)
    
    plt.figure(figsize=(fig_x, fig_y))
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    plt.xticks(x_ticks, fontsize=fs)
    plt.yticks(y_ticks, fontsize=fs)
    plt.xlabel(r'Density of states', fontsize=fs)
    plt.ylabel(r'Energy / eV', fontsize=fs)
    
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(lw)
    ax.spines['left'].set_linewidth(lw)
    ax.spines['right'].set_linewidth(lw)
    ax.spines['top'].set_linewidth(lw)
    
    plt.plot(y_1, x, "k", lw=lw, label=r'$\rm Total$')
    plt.plot(y_2, x, "#A2D063", lw=lw, label=r'$\rm Ti$')
    plt.plot(y_3, x, "#E9A7B3", lw=lw, label=r'$\rm O$')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc="center", ncol=4, borderaxespad=0., fontsize=fs)
    plt.axhline(0, ls='--', color='black',linewidth=lw)
    plt.savefig("./pdos-tot.png",dpi=800,bbox_inches = 'tight')
    return plt.show()
