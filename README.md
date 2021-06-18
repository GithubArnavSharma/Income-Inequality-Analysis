# Income-Inequality-Analysis
One of the biggest problems facing countries all around the world is income inequality. Income Inequality represents the inequality in the distribution of income throughout all residents in a country. High income inequality is generally linked to a worse country overall, and in general lower income inequality is advocated for. This statistical study analyzed how various factors could affect the economic health of a nation. 

The gini index is a useful tool to determine the income inequality of a country. A Gini coefficient of 0 would represent complete equality in the income of the population, and a Gini coefficient of 100 would represent complete inequality in the income of the population, where one person collects all the income. 

One research question to be asked is whether an increase in country investment(capital formation) would lead to less income inequality. However, when looking at data from 2017, it can be determined that simply increasing investment does not lead to a decrease in income inequality. 

When mapping 2017 data onto a regression plot, there looks to be no correlation between a nation's investment  as % of GDP and their gini index.

![investgini](https://user-images.githubusercontent.com/77365987/122496021-f14c6f00-cf9f-11eb-8a86-25f7a202bc5d.png)

When looking at the countries with the least income inequality, their investment as % of GDP is sparse.

![leastgini](https://user-images.githubusercontent.com/77365987/122496133-1b059600-cfa0-11eb-8dcb-c841fc727367.png)

When looking at countries with the most income inequality, their investment as % of GDP is also sparse.

![mostgini](https://user-images.githubusercontent.com/77365987/122496313-6324b880-cfa0-11eb-8370-73c1cc7c710c.png)

The results show that there are other factors to lead to less income inequality that are more important that simply the investment made by a country. In other words, increasing the capital formation in a nation does not translate to less income inequality.

Another research question to be asked is if there is a correlation between the tax revenue of a country and its income inequality. When looking at data from 2016, it can be determined that there is no correlation between tax revenue and income inequality.

When mapping the 2016 data onto a regression plot, there is shown no correlation between the gini index and tax revenue as % of GDP.

![taxgini](https://user-images.githubusercontent.com/77365987/122497758-c6afe580-cfa2-11eb-80bf-6748d5a482ea.png)

When looking at countries with the least income inequality, their tax revenue as % of GDP is sparse.

![leastginitax](https://user-images.githubusercontent.com/77365987/122497813-dcbda600-cfa2-11eb-9770-5ff94d2e1d51.png)

When looking at countries with the most income inequality, their tax revenue as % of GDP is also sparse.

![mostginitax](https://user-images.githubusercontent.com/77365987/122497848-e9da9500-cfa2-11eb-9c78-ef5deb7fadc2.png)

The results indicate that there are other factors that change the income inequality of a country than just tax revenue. Increasing the tax revenue of a country will not in of itself lead to a decrease in income inequality, and vice versa.

A third research question to explore is whether there is a correlation between the quality of the democracy of a country and its income inequality. A way to measure the quality of a democracy is through the EIU Democracy Index, which represents the quality of a nation's democracy as a number between 0 and 100. When looking at data from 2016, it can be determined that there is no correlation between democracy and income inequality.

When mapping the 2016 data onto a regression plot, there is shown a weak negative correlation between the gini index and a nation's democracy. This still remains not to be enough to hold any significant meaning. A Linear Regression algorithm trained to predict a gini index given the democracy level would only get an r2 score of ~0.03%. 

![democracygini](https://user-images.githubusercontent.com/77365987/122498489-13e08700-cfa4-11eb-9f28-e0c5a26e02fd.png)

All of these research questions showed that there is little correlation between a single variable and income inequality within a country. However, a question can be asked on whether or not the gini index is the best metric to the economic health of a country. Although higher income inequality is associated with the worsening of the economy of a country, this does not neccessarily mean that lower income inequality would lead to an increase in both the economy and the quality of living. As an example, Ukraine has the lowest income inequality in the world, yet has a poverty rate of over 50% as of 2021. 

Another way to measure the economic health of a country is rather the economic freedom of that country. Economic Freedom is an index that represents the ability of a population to make economic actions and control their own labor and property. 

Replacing the gini index with the economic freedom index and exploring the correlation between democracy and economic freedom shows a relatively strong postitive correlation between the democracy in a country and the country's economic freedom. 

When mapping 2016 on a regression plot, this correlation can be clearly shown.

![democracyfreedom](https://user-images.githubusercontent.com/77365987/122509594-e81bcc00-cfb8-11eb-9033-132168cb203b.png)

When looking at the countries with the least economic freedom, most have low democratic quality.

![leastfreedomdemocracy](https://user-images.githubusercontent.com/77365987/122509760-2a450d80-cfb9-11eb-9b2c-3fcd3215c36d.png)

When looking at the countries with the most economic freedom, they all have higher than average qualities of democracy.

![mostfreedomdemocracy](https://user-images.githubusercontent.com/77365987/122509783-38932980-cfb9-11eb-87a0-1dc646a8f17d.png)

It is clear there is a correlation between democracy and economic freedom. The population correlation between the two populations can be calculated as follows:

![correlation65](https://user-images.githubusercontent.com/77365987/122510370-5319d280-cfba-11eb-9210-4bf21fbb9d7c.png)

A 65.07% population correlation represents a high correlation, and shows that the relationship between democracy and economic freedom is strong. This is logical, as leaders are more likely to increase the ability of their population to make economic decisions if their leadership is more dependent on the population through democracy. 

All in all, a country can increase its economic freedom by giving the population more democratic power to elect politicians who are incentivized to increase their economic freedom. 
