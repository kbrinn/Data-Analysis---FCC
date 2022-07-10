import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    data_frame = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data_frame['Year'], data_frame['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res_1 = linregress(data_frame['Year'], data_frame['CSIRO Adjusted Sea Level'])
    x_line_1 = np.arange(1880, 2051, 1)
    y_line_1 = res_1.intercept + res_1.slope * x_line_1

    plt.plot(x_line_1, y_line_1, 'r', label='fitted line 1875 - 2050')

    # Create second line of best fit
    data_frame_2 = data_frame[data_frame['Year']>=2000]

    res_2 = linregress(data_frame_2['Year'], data_frame_2['CSIRO Adjusted Sea Level'])
    x_line_2 = np.arange(2000, 2051, 1)
    y_line_2 = res_2.intercept + res_2.slope * x_line_2

    plt.plot(x_line_2, y_line_2, 'g', label='fitted line 2020 -2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()