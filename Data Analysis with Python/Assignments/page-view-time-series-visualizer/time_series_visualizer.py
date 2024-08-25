import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'] )

# Clean data
df = df.loc[ (df['value'] >= df['value'].quantile(0.025)) &
            (df['value'] <= df['value'].quantile(0.975))
            ]


def draw_line_plot():
    # Draw line plot
    fig, ax1 = plt.subplots(figsize=(16,8))
    
    sns.lineplot(data = df, ax = ax1, x = df.index, y = 'value', color = 'red')
    
    ax1.set( title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
            xlabel = 'Date', ylabel = 'Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar.reset_index(inplace = True)

    df_bar_grouped = pd.DataFrame(df_bar.groupby(['year', 'month'], sort = False)['value'].mean().round())
    df_bar_grouped = df_bar_grouped.rename(columns={'value': 'average views'})
    df_bar_grouped.reset_index(inplace = True)
    
    # Add missing values
    missing_df = pd.DataFrame({'year':[2016, 2016, 2016, 2016], 'month':['January','February','March','April'], 'average views':[0,0,0,0]} )
    df_bar_tot = pd.concat([missing_df, df_bar_grouped], ignore_index = True)

    # Draw bar plot
    fig, ax1 = plt.subplots(figsize=(16,8))
    sns.barplot(ax = ax1, data = df_bar_tot, x = 'year', y = 'average views',
                hue = 'month', palette = 'bright')

    ax1.set(title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
            xlabel='Years', ylabel = 'Average Page Views')
    
    ax1.legend(title = 'Months', loc='upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order = [pd.to_datetime(f'2023-{i}-01').strftime('%b') for i in range(1, 13)]     
    
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    sns.boxplot(data=df_box, ax=ax1, x='year', y='value', palette='Set2')
    ax1.set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
    
    sns.boxplot(data=df_box, ax=ax2, x='month', y='value', palette='Set2')
    ax2.set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
