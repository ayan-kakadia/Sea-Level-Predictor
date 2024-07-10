import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    line_out1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    slope1 = line_out1[0]
    intercept1 = line_out1[1]
    year = np.arange(1880, 2051)
    line1 = year * slope1 + intercept1
    plt.plot(year, line1)


    # Create second line of best fit
    df2 = df[df["Year"] >=2000]
    line_out2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    slope2 = line_out2[0]
    intercept2 = line_out2[1]
    year = np.arange(2000, 2051)
    line2 = year * slope2 + intercept2
    plt.plot(year, line2)


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()