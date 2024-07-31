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
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'], alternative='two-sided')
    x1 = np.arange(df['Year'].min(),2051)
    best_fit_line = line1.slope*x1+line1.intercept
    plt.plot(x1, best_fit_line, color='firebrick') # 1st best fit

    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    line2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'], alternative='two-sided')
    x2 = np.arange(df2['Year'].min(), 2051)
    second_best_fit_line = line2.slope*x2+line2.intercept
    plt.plot(x2, second_best_fit_line, color='limegreen')# 2nd best fit

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()