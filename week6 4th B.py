import pandas as pd
import matplotlib.pyplot as m
import seaborn as s

# --- Load and preprocess the data ---
da = pd.read_csv("matches.csv")

# Check for and drop missing values
da.drop('umpire3', axis=1, inplace=True)
da.dropna(axis=0, inplace=True)

# --- Plotting Functions ---

# Function to create a histogram
def histo(da, col, title, xlabel):
    m.figure(figsize=(8, 6))
    s.histplot(da[col], bins=20, kde=True)
    m.title(title)
    m.xlabel(xlabel)
    m.ylabel('Frequency')
    m.show()

# Function to create a count plot
def count_plo(da, x, title, xlabel):
    m.figure(figsize=(15, 7))
    s.countplot(x=x, data=da, palette='Set2')
    m.title(title)
    m.xlabel(xlabel)
    m.ylabel('Count')
    m.xticks(rotation=90)
    m.tight_layout()
    m.show()

# Function to create a stacked bar chart
def sta_bar(da, x, y, title, xlabel, ylabel, legend_title=None):
    dp = da.groupby([x, y]).size().unstack()
    dp.plot(kind='bar', stacked=True, figsize=(10, 6))
    m.title(title)
    m.xlabel(xlabel)
    m.ylabel(ylabel)
    if legend_title:
        m.legend(title=legend_title)
    m.show()

# --- Data Exploration ---

histo(da, 'win_by_runs', 'Distribution of Win by Runs', 'Win by Runs')
histo(da, 'win_by_wickets', 'Distribution of Win by Wickets', 'Win by Wickets')

count_plo(da, 'city', 'Count of Matches at Each City', 'City')
count_plo(da, 'winner', 'Count of Winning of Each Team', 'Team')

sta_bar(da, 'toss_decision', 'result', 'Toss Decision vs. Match Result',
         'Toss Decision', 'Count', legend_title='Match Result')

sta_bar(da, 'season', 'toss_decision', 'Season-wise Toss Decision',
         'Season', 'Count', legend_title='Toss Decision')
