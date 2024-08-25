import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x= df['Year'], y = df['CSIRO Adjusted Sea Level'], label = 'original data')
    ax.set(title = 'Rise in Sea Level', 
           xlabel = 'Year', ylabel = 'Sea Level (inches)')
    ax.legend()


    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit.
    # Plot the line of best fit over the top of the scatter plot.
    # Make the line go through the year 2050 to predict the sea level rise in 2050.
    
    regr = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    m1 = regr.slope
    q1 = regr.intercept
    
    x1 = pd.Series([ i for i in range(1880,2051, 1)])
    
    ax.plot(x1, m1*x1 + q1, color = 'r', label = 'first prediction')
    ax.legend()
    
    # Create second line of best fit
    # Plot a new line of best fit just using the data from year 2000 
    # through the most recent year in the dataset.
    # Make the line also go through the year 2050 to predict the sea level rise in 2050 
    # if the rate of rise continues as it has since the year 2000.
    
    df_recent = df.loc[df['Year']>=2000, :]
    
    regr = linregress(x=df_recent['Year'], y=df_recent['CSIRO Adjusted Sea Level'])
    m2 = regr.slope
    q2 = regr.intercept
    
    x2 = pd.Series([ i for i in range(2000,2051, 1)])
    
    ax.plot(x2, m2*x2 + q2, color = 'g', label = 'second prediction')
    ax.legend()
    


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()