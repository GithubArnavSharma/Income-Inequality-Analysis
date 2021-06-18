#------------------Find the relationship between Country Investment as % of GDP and the Gini Index------------------# 

#Import neccessary modules 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read the datasets for the gini index and investment
gini = pd.read_csv('gini.csv')
invest = pd.read_csv('investment.csv')

#Preform data cleaning
gini = gini.melt(id_vars=['country'], var_name='Year')
invest = invest.melt(id_vars=['country'], var_name='Year')

gini['Year'] = gini['Year'].apply(lambda x: int(x))
gini = gini[gini['Year'] > 1959]
gini = gini[gini['Year'] < 2018]
invest['Year'] = invest['Year'].apply(lambda x: int(x))

#Get a list of all the countries and years that do not have NaN 
invest = invest[invest['value'].notna()]
invest_list = np.array(invest[['country', 'Year']])
invest_list = [list(i) for i in invest_list]

#Remove the countries from the gini index that have NaN in the investment dataset
index_drop = []
for i in range(len(gini)):
    gini_i = list(np.ravel(np.array(gini.iloc[[i]][['country', 'Year']])))
    if gini_i not in invest_list:
        index_drop.append(31200+i)
gini = gini.drop(index_drop)

#Get the data from the year 2017 on the data
gini_2017 = np.array(gini[gini['Year']==2017])[:, 2]
invest_2017 = np.array(invest[invest['Year']==2017])[:, 2]

gini_2017 = gini_2017.astype(np.float32)
invest_2017 = invest_2017.astype(np.float32)

#Make a regression plot exploring the relationship between a countries investment and its income inequality 
df = pd.DataFrame({'Gini Index':gini_2017, 'Invest % of GDP':invest_2017})
sns.set_theme()
sns.regplot(x='Invest % of GDP', y='Gini Index', data=df)
plt.show()

#Get the investment data from the countries with the lowest income inequality 
lowest_gini = np.sort(gini_2017)[:10]
lowest_index = [list(gini_2017).index(low) for low in lowest_gini]
gini_invest = [invest_2017[index] for index in lowest_index]
gini_invest = gini_invest + [np.median(invest_2017)]

country = [np.array(gini[gini['Year']==2017]['country'])[index] for index in lowest_index]
for i in range(len(country)):
    if 'Central' in country[i]:
        country[i] = 'CAR'
country = country + ['Average']

#Show that data in a bar plot 
df = pd.DataFrame({'Countries w/ least gini(ordered from least)':country, 'Invest % of GDP':gini_invest})
graph = sns.barplot(x='Countries w/ least gini(ordered from least)', y='Invest % of GDP', data=df, palette='Blues_d')
graph.axhline(gini_invest[-1], c='red', lw=2)
plt.show()

#Get the investment data from the countries with the highest income inequality 
large_gini = np.sort(gini_2017)[-10:]
highest_index = [list(gini_2017).index(high) for high in large_gini]
gini_invest = [invest_2017[index] for index in highest_index]
gini_invest = gini_invest + [np.median(invest_2017)]

country = [np.array(gini[gini['Year']==2017]['country'])[index] for index in highest_index]
for i in range(len(country)):
    if 'Central' in country[i]:
        country[i] = 'CAR'
country = country + ['Average']

#Show that data in a bar plot 
df = pd.DataFrame({'Countries w/ most gini(ordered from least)':country, 'Invest % of GDP':gini_invest})
graph = sns.barplot(x='Countries w/ most gini(ordered from least)', y='Invest % of GDP', data=df, palette='rocket')
graph.axhline(gini_invest[-1], c='blue', lw=2)
plt.show()
