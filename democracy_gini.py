import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gini = pd.read_csv('gini.csv')
democracy = pd.read_csv('democracy.csv')

gini = gini.melt(id_vars=['country'], var_name='Year')
democracy = democracy.melt(id_vars=['country'], var_name='Year')

gini['Year'] = gini['Year'].apply(lambda x: int(x))
gini = gini[gini['Year'] > 1959]
gini = gini[gini['Year'] < 2018]

democracy['Year'] = democracy['Year'].apply(lambda x: int(x))
democracy = democracy[democracy['value'].notna()]
democracy_list = np.array(democracy[['country', 'Year']])
democracy_list = [list(i) for i in democracy_list]

index_drop = []
for i in range(len(gini)):
    gini_i = list(np.ravel(np.array(gini.iloc[[i]][['country', 'Year']])))
    if gini_i not in democracy_list:
        index_drop.append(31200+i)
gini = gini.drop(index_drop)

gini.to_csv('new_gini1.csv', index=False)

gini = pd.read_csv('new_gini1.csv')

gini_2016 = np.array(gini[gini['Year']==2016])[:, 2]
democracy_2016 = np.array(democracy[democracy['Year']==2016])[:, 2]

gini_2016 = gini_2016.astype(np.float32)
democracy_2016 = democracy_2016.astype(np.float32)

df = pd.DataFrame({'Gini Index':gini_2016, 'Democracy Index':democracy_2016})
sns.set_theme()
sns.regplot(x='Democracy Index', y='Gini Index', data=df)
plt.show()
