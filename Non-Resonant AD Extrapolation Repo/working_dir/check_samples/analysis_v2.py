import numpy as np
import matplotlib.pyplot as plt
from utils import *
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "-s",
    "--sigsample",
    action="store",
    help="Path to the signal sample .txt file.",
    default="../samples/sig_samples/rinv13_13TeV_v1.txt"
)
parser.add_argument(
    "-b",
    "--bkgsample",
    action="store",
    help="Path to the background sample .txt file.",
    default="../samples/qcd_data_samples/qcd_0.txt"
)
parser.add_argument(
    "-mc",
    "--mcsample",
    action="store",
    help="Path to the MC sample .txt file.",
    default="../samples/qcd_mc_samples/qcd_0.txt"
)
parser.add_argument(
    "-o",
    "--outdir",
    action="store",
    default="outputs",
    help="Output directory for the plots.",
)
args = parser.parse_args()

def main():
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)
    
    # Load samples
    variables, sig = load_samples(args.sigsample)
    _, bkg = load_samples(args.bkgsample)
    _, mc = load_samples(args.mcsample)
    
    labels_list = [r"$Z' \to jj$, $m_{Z'} = 4$ TeV", "QCD dijet (data)", "QCD dijet (sim)"]
    
    names = name_map()
    units = unit_map()

    # Define figure layout (number of subplots)
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))  # Change number of subplots for your variables
    plt.subplots_adjust(wspace=0.3)  # Adjust spacing between plots
    
    for i, x in enumerate(['ht', 'met']):
        ind_x = ind(variables, x)
        sig_x = sig[:, ind_x]
        bkg_x = bkg[:, ind_x]
        mc_x = mc[:, ind_x]
        
        title = f"{names[x]} distribution"
        xlabel = f"{names[x]} {units[x]}"
        
        # Define bins
        if x == 'ht':
            bins = np.linspace(0, 4000, 26)
        elif x == 'met':
            bins = np.linspace(0, 600, 26)
        
        # Plot data
        axs[i].hist(bkg_x, bins=bins, label=labels_list[1], histtype='stepfilled', color='cyan', alpha=0.5)
        axs[i].hist(mc_x, bins=bins, label=labels_list[2], histtype='step', color='green', linewidth=1.5)
        axs[i].hist(sig_x, bins=bins, label=labels_list[0], histtype='step', color='orange', linewidth=1.5)
        
        axs[i].set_title(title, fontsize=12)
        axs[i].set_xlabel(xlabel, fontsize=10)
        axs[i].set_ylabel("a.u.", fontsize=10)
        
        # Add SR cut lines (adjust for each plot accordingly)
        if x == 'ht':
            axs[i].axvline(x=800, color='black', linestyle='--', label="SR cuts")
        elif x == 'met':
            axs[i].axvline(x=75, color='black', linestyle='--')
        
    # Add legend to one of the plots and position it outside
    axs[0].legend(loc='upper right', fontsize=8, frameon=False)
    
    plt.savefig(f"{outdir}/comparison_plot.png")
    plt.show()

if __name__ == "__main__":
    main()

