#------------------Explore the relationship between the democratic quality of countries and their economic freedom 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read and clean the data 
freedom = pd.read_csv('freedom.csv')
democracy = pd.read_csv('democracy.csv')

democracy = democracy.melt(id_vars=['country'], var_name='Year')

freedom['Year'] = freedom['Year'].apply(lambda x: int(x))
democracy['Year'] = democracy['Year'].apply(lambda x: int(x))

#Store info on the parts of the democratic dataset that have NaN 
democracy = democracy[democracy['Year']==2016]
democracy = democracy[democracy['value'].notna()]
democracy_list = np.array(democracy[['country', 'Year']])
democracy_list = [list(i) for i in democracy_list]

#Remove countries from the economic freedom dataset that have no info on the democratic one 
index_drop = []
for i in range(len(freedom)):
    freedom_i = list(np.ravel(np.array(freedom.iloc[[i]][['country', 'Year']])))
    if freedom_i not in democracy_list:
        index_drop.append(i)
freedom = freedom.drop(index_drop)

#Repeat the same process but for the datasets reversed 
freedom = freedom.sort_values('country')
freedom_list = np.array(freedom[['country', 'Year']])
freedom_list = [list(i) for i in freedom_list]

index_drop = []
for i in range(len(democracy)):
    dem_i = list(np.ravel(np.array(democracy.iloc[[i]][['country', 'Year']])))
    if dem_i not in freedom_list:
        index_drop.append(1640+i)
democracy = democracy.drop(index_drop)

#Collect the data from the economic freedom and democratic index of countries in 2016
freedom_2016 = np.array(freedom[freedom['Year']==2016])[:, 1]
democracy_2016 = np.array(democracy[democracy['Year']==2016])[:, 2]

freedom_2016 = freedom_2016.astype(np.float32)
democracy_2016 = democracy_2016.astype(np.float32)

#Make a regression plot showcasing the relationship between democracy and economic freedom 
df = pd.DataFrame({'Economic Freedom Index':freedom_2016, 'Democracy Index':democracy_2016})
sns.set_theme()
sns.regplot(x='Democracy Index', y='Economic Freedom Index', data=df)
plt.show()

#Get the democratic index of the countries with the lowest economic freedom 
lowest_freedom = np.sort(freedom_2016)[:10]
lowest_index = [list(freedom_2016).index(low) for low in lowest_freedom]
freedom_democracy = [democracy_2016[index] for index in lowest_index]
freedom_democracy = freedom_democracy + [np.median(democracy_2016)]

country = [np.array(freedom[freedom['Year']==2016]['country'])[index] for index in lowest_index]
country = country + ['Average']
for i in range(len(country)):
    if 'Central' in country[i]:
        country[i] = 'CAR'

#Show that data in a bar plot 
df = pd.DataFrame({'Countries w/ least economic freedom(ordered from least)':country, 'Democracy Index':freedom_democracy})
graph = sns.barplot(x='Countries w/ least economic freedom(ordered from least)', y='Democracy Index', data=df, palette='Blues_d')
graph.axhline(freedom_democracy[-1], c='red', lw=2)
plt.show()

#Get the democratic index of the countries with the highest economic freedom
large_freedom = np.sort(freedom_2016)[-10:]
highest_index = [list(freedom_2016).index(high) for high in large_freedom]
freedom_democracy = [democracy_2016[index] for index in highest_index]
freedom_democracy = freedom_democracy + [np.median(democracy_2016)]

country = [np.array(freedom[freedom['Year']==2016]['country'])[index] for index in highest_index]
for i in range(len(country)):
    if 'Central' in country[i]:
        country[i] = 'CAR'
country = country + ['Average']

#Showcase that data in a bar plot 
df = pd.DataFrame({'Countries w/ most economic freedom(ordered from least)':country, 'Democracy Index':freedom_democracy})
graph = sns.barplot(x='Countries w/ most economic freedom(ordered from least)', y='Democracy Index', data=df, palette='rocket')
graph.axhline(freedom_democracy[-1], c='blue', lw=2)
plt.show()

