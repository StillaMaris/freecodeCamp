import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Importa dati
df = pd.read_csv('medical_examination.csv')

# 2 Define a new column that says if someone is overweight
bmi_calculation = df['weight'] / (df['height']/100)**2 
df['overweight'] = [1 if bmi > 25 else 0 for bmi in bmi_calculation]

# 3 Normalize data
df['cholesterol'] = [1 if col > 1 else 0 for col in df['cholesterol']]
df['gluc'] = [1 if g > 1 else 0 for g in df['gluc']]



# 4
def draw_cat_plot():
    # 5
    x_ticks = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(
            df, 
            id_vars='cardio',  # Keep 'cardio' as identifier
            value_vars= x_ticks
            )
    

    # 6
    # Group and reformat the data in df_cat to split it by cardio
    df_cat_grouped = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7 Plot
    # Create a catplot
    figure = sns.catplot(data=df_cat_grouped,
                      x='variable',
                      y='total',
                      hue='value',
                      col='cardio',  # Split by 'cardio'
                      kind='bar'
                    )
    
    # 8 (optional adjustments, such as titles, labels, etc.)
    fig = figure.fig
    # 9 Save the figure
    fig.savefig('catplot.png')

    return fig


# 10
def draw_heat_map():
    # 11 Clean data

    height_lower_bound = df['height'].quantile(0.025)
    height_upper_bound = df['height'].quantile(0.975)

    weight_lower_bound = df['weight'].quantile(0.025)
    weight_upper_bound = df['weight'].quantile(0.975)

    # Filter the DataFrame based on height, weight, and pressure conditions
    df_heat = df[(df['height'] >= height_lower_bound) & 
                        (df['height'] <= height_upper_bound) &
                        (df['weight'] >= weight_lower_bound) & 
                        (df['weight'] <= weight_upper_bound) &
                        (df['ap_lo'] <= df['ap_hi'])]  # Ensure diastolic pressure is not higher than systolic

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))



    # 14
    fig, ax = plt.subplots(figsize = (10,8))

    # 15
    sns.heatmap(corr,
                mask=mask,
                annot = True,
                fmt = '0.1f', 
                vmin = -0.16, vmax = 0.32,
                linewidths= 0.5,
                center = 0
            )


    # 16
    fig.savefig('heatmap.png')
    return fig
