#------------------Explore the relationship between a countries tax revenue and its gini index------------------#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read and clean the data 
gini = pd.read_csv('gini.csv')
tax = pd.read_csv('tax.csv')

gini = gini.melt(id_vars=['country'], var_name='Year')
tax = tax.melt(id_vars=['country'], var_name='Year')

gini['Year'] = gini['Year'].apply(lambda x: int(x))
tax['Year'] = tax['Year'].apply(lambda x: int(x))
gini = gini[gini['Year'] > 1959]
gini = gini[gini['Year'] < 2018]

#Collect a list containing info of the countries that don't have NaN
tax = tax[tax['value'].notna()]
tax_list = np.array(tax[['country', 'Year']])
tax_list = [list(i) for i in tax_list]

#Remove the countries from the gini dataset that the tax dataset has no info for 
index_drop = []
for i in range(len(gini)):
    gini_i = list(np.ravel(np.array(gini.iloc[[i]][['country', 'Year']])))
    if gini_i not in tax_list:
        index_drop.append(31200+i)
gini = gini.drop(index_drop)

#Get the data on the gini index and tax revenue for 2016
gini_2016 = np.array(gini[gini['Year']==2016])[:, 2]
tax_2016 = np.array(tax[tax['Year']==2016])[:, 2]

gini_2016 = gini_2016.astype(np.float32)
tax_2016 = tax_2016.astype(np.float32)

#Create a regression plot showcasing the relationship between a countries tax revenue and its income inequality 
df = pd.DataFrame({'Gini Index':gini_2016, 'Tax Rev % of GDP':tax_2016})
sns.set_theme()
sns.regplot(x='Tax Rev % of GDP', y='Gini Index', data=df)
plt.show()

#Get data on the tax revenue of the countries with the lowest income inequality 
lowest_gini = np.sort(gini_2016)[:10]
lowest_index = [list(gini_2016).index(low) for low in lowest_gini]
gini_tax = [tax_2016[index] for index in lowest_index]
gini_tax = gini_tax + [np.median(tax_2016)]

country = [np.array(gini[gini['Year']==2016]['country'])[index] for index in lowest_index]
for i in range(len(country)):
    if 'Central' in country[i]:
        country[i] = 'CAR'
country = country + ['Average']

#Show that data in a bar plot 
df = pd.DataFrame({'Countries w/ least gini(ordered from least)':country, 'Tax % of GDP':gini_tax})
graph = sns.barplot(x='Countries w/ least gini(ordered from least)', y='Tax % of GDP', data=df, palette='Blues_d')
graph.axhline(gini_tax[-1], c='red', lw=2)
plt.show()

#Get data on the tax revenue of the countries with the greatest income inequality 
large_gini = np.sort(gini_2016)[-10:]
highest_index = [list(gini_2016).index(high) for high in large_gini]
gini_tax = [tax_2016[index] for index in highest_index]
gini_tax = gini_tax + [np.median(tax_2016)]

country = [np.array(gini[gini['Year']==2016]['country'])[index] for index in highest_index]
for i in range(len(country)):
    if 'Central' in country[i]:
        country[i] = 'CAR'
country = country + ['Average']

#Show that data in a bar plot 
df = pd.DataFrame({'Countries w/ most gini(ordered from least)':country, 'Tax % of GDP':gini_tax})
graph = sns.barplot(x='Countries w/ most gini(ordered from least)', y='Tax % of GDP', data=df, palette='rocket')
graph.axhline(gini_tax[-1], c='blue', lw=2)
plt.show()
