# -*- coding: utf-8 -*-
"""Test script module for heatmap4kmers package

Test module demonstrates the example charts for kmeRs package 
and checks the package integrity

"""
## (C) Rafal Urniaz

# Import modules
import heatmap4kmers

try:
    from kmers_heatmap import kmers_heatmap
    from kmers_heatmap import read_file

    # Graphics 
    import matplotlib.pyplot as plt

    #import matplotlib_heatmap_functions
    print("import: [-- OK --]")
except ImportError:
    print("Could not import heatmap4kmers package [-- Error --]")


if __name__ == '__main__':

# --- Import sample_file 
    try:
        x = read_file(filename = r"example_data\example_kmeRs_matrix.csv")
        print("Load demo dataframe [-- OK --]")
# --- Prepare Quick HeatMap Demo

# Standard
        kmers_heatmap(file_dataframe = x, show_legend = False, save_file = True, file_name = "Figure_1.png")
        print("Save demo plot as Figure_1.png [-- OK --]")
# Categorised
        kmers_heatmap(file_dataframe = x, cmap = plt.cm.get_cmap('Blues', 10), save_file = True, file_name = "Figure_2.png")
        print("Save demo plot as Figure_2.png [-- OK --]")
# RdBu positive vs. negative values
        kmers_heatmap(file_dataframe = x[x.columns.difference(["score_total"])], cmap="RdBu", save_file = True, file_name = "Figure_3.png")
        print("Save demo plot as Figure_3.png [-- OK --]")
    except:
        print("Test not pass [-- Error --]")