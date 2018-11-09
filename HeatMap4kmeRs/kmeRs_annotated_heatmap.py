# (C) Rafal Urniaz
#  

# Import required modules
import os, csv, sys

# Data 
import numpy as np
import pandas as pd

# Graphics 
import matplotlib
import matplotlib.pyplot as plt

# External
import matplotlib_heatmap_functions

# Function takes as an argument the filename and directory 
# and returns pandas' dataframe

def read_file(filename = ""):

    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        file_dataframe = pd.read_csv(filename, sep = ";", index_col = 0)
        file_dataframe = pd.DataFrame(file_dataframe.iloc[1:len(file_dataframe.iloc[0])], dtype = "float_")
        print("File exists and is readable [-- OK --]")

        # Print first 5 rows
        print(file_dataframe.iloc[0:3,])
    
    else:
        print("Either the file is missing or not readable")
        sys.exit()
    
    return file_dataframe


# Prepare data function takes as an argument the read_file() function
# output and returns list of dataframe

def prepare_data(file_dataframe):

    # x axis labels - columns names
    x_labels = file_dataframe.columns

    # y axis label - rows names
    y_labels = file_dataframe.index

    # data to the heatmap plot
    data = file_dataframe.values

    return [x_labels, y_labels, data]


# Save heatmap in location defined by filename 

def save_or_show_heatmap(plt, show = True, file_name = ""):

    # Show = True
    if show == True:
        plt.show()
    if show == False:
        plt.savefig(file_name)
    return ""


# Prepare data function takes as an argument the read_file() function
# output and returns list of dataframe

def quick_kmeRs_heatmap(file_dataframe, title = "Example GATTACA HeatMap", show = True, file_name = ""):

# Prepare data
    
    x = prepare_data(file_dataframe)

    x_labels = x[0]
    y_labels = x[1]
    data = x[2]

# Prepare HeatMap

    fig, ax = plt.subplots()
    im = ax.imshow(data)

# -- Lablels --

    # Show all ticks
    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_yticks(np.arange(len(y_labels)))

    # Label with the respective list entries
    ax.set_xticklabels(x_labels)
    ax.set_yticklabels(y_labels)

    # Rotate 45 degrees the labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(y_labels)):
        for j in range(len(x_labels)):
            ax.text(j, i, data[i, j],ha="center", va="center", color="w")

    ax.set_title(title)


    fig.tight_layout()

# Save or show the plot

    save_or_show_heatmap(plt, show, file_name)

    return "Done!"