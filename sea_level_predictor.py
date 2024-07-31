import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure(figsize=(9,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10)

    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()