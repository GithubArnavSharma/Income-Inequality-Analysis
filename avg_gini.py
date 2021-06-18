#Import neccessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read the gini csv
gini = pd.read_csv('gini.csv')

#Collect data needed for the line plot on the average gini index and of USA
years = np.array([col for col in gini.columns[1:] if int(col) % 5 == 0 and int(col) > 1955 and int(col) < 2020])
avg_year = [np.mean(gini[year]) for year in years] + [float(gini[gini['country'] == 'United States'][year]) for year in years]
all_country = ['All countries' for i in range(len(years))] + ['USA' for i in range(len(years))]
all_year = list(years) * 2

#Use that data to make a line plot 
df = pd.DataFrame({'Country':all_country, 'Year':all_year, 'Gini Index':avg_year})
sns.set_theme()
sns.lineplot(x='Year', y='Gini Index', hue='Country', data=df)
plt.show()
