import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index = pd.to_datetime(df.index)

#print(df)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025) ) & (df['value'] <= df['value'].quantile(0.975))]
#print(df)


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15,5))
    plt.plot(df.index, df['value'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

#draw_line_plot()


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    

    
    # Draw bar plot
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    df_bar = df_bar.sort_index(axis=1)

    fig, ax = plt.subplots(figsize=(12, 6))

    df_bar.plot(kind='bar', ax=ax)

    ax.set_xlabel('Years')

    ax.set_ylabel('Average Page Views')

    plt.tight_layout()

    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

#draw_bar_plot()

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%B') for d in df_box.date]

    ordered_months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    df_box['month'] = pd.Categorical(df_box['month'], categories=ordered_months, ordered=True)


    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], color='white', fliersize=1, linewidth=1)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')



    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1],  color='white', fliersize=1, linewidth=1) 
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()



    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()