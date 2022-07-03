import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    fig,ax = plt.subplots(figsize=(22,8), dpi=80)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.plot(df.index, df['value'], color='blue', linewidth=2)
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

  
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['time'] = df.index.astype('datetime64[ns]')
    df['Years'] = pd.DatetimeIndex(df['time']).year
    df['Months'] = pd.DatetimeIndex(df['time']).month
    df_bar = df.groupby(['Years','Months'])['value'].mean()
    df_bar = df_bar.unstack()
    df['Months'] = df['Months'].map({1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'})
    label_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    fig = df_bar.plot(kind='bar', figsize=(22,8)).figure
    plt.title('Average Page Views by Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    graph_legend = plt.legend(title = 'Months', fontsize = '12',labels = label_months)
    title = graph_legend.get_title()
    title.set_fontsize('12')
    # Draw bar plot
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df['time'] = df.index.astype('datetime64[ns]')
    df['Month'] = pd.DatetimeIndex(df['time']).month
    df['Year'] = pd.DatetimeIndex(df['time']).year
    df['Month'] = df['Month'].map({1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'})

    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig,axes = plt.subplots(1,2, figsize=(38,12), dpi=80)


    sns.boxplot(x='Year', y='value', data=df, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Draw box plots (using Seaborn)
    sns.boxplot(x='Month', y='value', data=df, ax=axes[1] ,order=month_list)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig