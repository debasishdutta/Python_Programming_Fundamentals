""" ######################################################################### """
""" ################################# LINE PLOTS ############################ """
""" ######################################################################### """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import matplotlib.mlab as mlab
import seaborn as sns
import os
home_dir = "C:/Users/debas/Downloads/Python Code Library/Numpy, Pandas, Matplotlib, Bokeh/Datasets"
os.chdir(home_dir)

""" Multiple Line Plots """
stock_data = pd.read_csv("8_Four Stocks.csv", parse_dates=True).iloc[:10,:]

plt.plot(stock_data.iloc[:,0],stock_data.iloc[:,1],
         marker='o', markerfacecolor='skyblue', markersize=8, 
         linestyle='-',color='skyblue', linewidth=2)

plt.plot(stock_data.iloc[:,0],stock_data.iloc[:,2],
         marker='*', markerfacecolor='olive', markersize=8, 
         linestyle='--',color='olive', linewidth=2)

plt.plot(stock_data.iloc[:,0],stock_data.iloc[:,3],
         marker='+', markerfacecolor='green', markersize=8, 
         linestyle='-.',color='green', linewidth=2)

plt.plot(stock_data.iloc[:,0],stock_data.iloc[:,4],
         marker='x', markerfacecolor='red', markersize=8, 
         linestyle=':',color='red', linewidth=2)

plt.xlabel("Date")
plt.ylabel("Stock Price In USD")
plt.title("Stock Price Movement")
plt.legend(['Apple', 'IBM', 'Cisco', 'Microsoft'], loc='lower right')
fig=plt.figure(dpi=100)
fig.set_figheight(20)
fig.set_figwidth(30)
fig.show()

""" Sub Plots [nrows, ncols, index] (Line Plots) """
plt.subplot(2,2,1)
plt.plot(stock_data.iloc[:,0],stock_data.iloc[:,1],
         marker='o', markerfacecolor='skyblue', markersize=8, 
         linestyle='-',color='skyblue', linewidth=2)
plt.xticks(stock_data.iloc[::2,0],["Jan-3","Jan-5","Jan-7","Jan-11","Jan-13" ])
plt.xlabel("Date")
plt.ylabel("Stock Price In USD")
plt.title("Apple")
plt.subplot(2,2,2)
plt.plot(stock_data.iloc[:,0],stock_data.iloc[:,2],
         marker='o', markerfacecolor='olive', markersize=8, 
         linestyle='-',color='olive', linewidth=2)
plt.xticks(stock_data.iloc[::2,0],["Jan-3","Jan-5","Jan-7","Jan-11","Jan-13" ])
plt.xlabel("Date")
plt.ylabel("Stock Price In USD")
plt.title("IBM")
plt.subplot(2,2,3)
plt.plot(stock_data.iloc[:,0],stock_data.iloc[:,3],
         marker='o', markerfacecolor='green', markersize=8, 
         linestyle='-',color='green', linewidth=2)
plt.xticks(stock_data.iloc[::2,0],["Jan-3","Jan-5","Jan-7","Jan-11","Jan-13" ])
plt.xlabel("Date")
plt.ylabel("Stock Price In USD")
plt.title("Cisco")
plt.subplot(2,2,4)
plt.plot(stock_data.iloc[:,0],stock_data.iloc[:,4],
         marker='x', markerfacecolor='red', markersize=8, 
         linestyle='-',color='red', linewidth=2)
plt.xticks(stock_data.iloc[::2,0],["Jan-3","Jan-5","Jan-7","Jan-11","Jan-13" ])
plt.xlabel("Date")
plt.ylabel("Stock Price In USD")
plt.title("Microsoft")
plt.tight_layout()
plt.show()

""" Customizing Line Plot Axis """
gdp_data = pd.read_csv("11_GDP.csv")

plt.subplot(3,2,1)
plt.plot(gdp_data.iloc[:,0], gdp_data.iloc[:,1],
         marker='x', markerfacecolor='red', markersize=8, 
         linestyle='-',color='red', linewidth=2)
plt.xlim((1960, 1970))
plt.ylim((40, 100))
plt.xlabel('Year')
plt.ylabel('Billions of Dollars')
plt.title('China Gross Domestic Product')

plt.subplot(3,2,2)
plt.plot(gdp_data.iloc[:,0], gdp_data.iloc[:,1],
         marker='x', markerfacecolor='red', markersize=8, 
         linestyle='-',color='red', linewidth=2)
plt.xlim((1971, 1980))
plt.ylim((100, 200))
plt.xlabel('Year')
plt.ylabel('Billions of Dollars')
plt.title('China Gross Domestic Product')

plt.subplot(3,2,3)
plt.plot(gdp_data.iloc[:,0], gdp_data.iloc[:,1],
         marker='x', markerfacecolor='red', markersize=8, 
         linestyle='-',color='red', linewidth=2)
plt.xlim((1981, 1990))
plt.ylim((200, 360))
plt.xlabel('Year')
plt.ylabel('Billions of Dollars')
plt.title('China Gross Domestic Product')

plt.subplot(3,2,4)
plt.plot(gdp_data.iloc[:,0], gdp_data.iloc[:,1],
         marker='x', markerfacecolor='red', markersize=8, 
         linestyle='-',color='red', linewidth=2)
plt.xlim((1991, 2000))
plt.ylim((350, 1210))
plt.xlabel('Year')
plt.ylabel('Billions of Dollars')
plt.title('China Gross Domestic Product')

plt.subplot(3,2,5)
plt.plot(gdp_data.iloc[:,0], gdp_data.iloc[:,1],
         marker='x', markerfacecolor='red', markersize=8, 
         linestyle='-',color='red', linewidth=2)
plt.xlim((2001, 2010))
plt.ylim((1300, 6100))
plt.xlabel('Year')
plt.ylabel('Billions of Dollars')
plt.title('China Gross Domestic Product')

plt.subplot(3,2,6)
plt.plot(gdp_data.iloc[:,0], gdp_data.iloc[:,1],
         marker='x', markerfacecolor='red', markersize=8, 
         linestyle='-',color='red', linewidth=2)
plt.xlim((2011, 2015))
plt.ylim((7400, 11000))
plt.xlabel('Year')
plt.ylabel('Billions of Dollars')
plt.title('China Gross Domestic Product')
plt.tight_layout()
plt.show()

""" ######################################################################### """
""" ######################## SCATTERED/ BUBBLE PLOTS ######################## """
""" ######################################################################### """

""" Group By Scattered Plot """
test_scores  = pd.read_csv("11_Test Scores.csv")
test_scores['Gender']=pd.Categorical(test_scores['Gender'])
groups = test_scores.groupby('Gender')

for name, group in groups:
    plt.style.use('ggplot')
    plt.scatter(group.preTestScore,
                group.postTestScore,
                s=group.age*5,
                label=name, 
                alpha=0.7,
                edgecolors="k",
                linewidth=1.5)
    plt.legend(numpoints=2, loc='lower right', frameon=True, title="Gender")
plt.xlabel('Pre Test Score')
plt.ylabel('Post Test Score')
plt.title('Scattered Plot')
plt.show()

""" Color Map For Continous Variable """
gapminder_data = pd.read_csv("11_Gapminder.csv")

plt.scatter(x=gapminder_data['pop']/(10**9), 
            y=gapminder_data['lifeExp'], 
            c=gapminder_data['pop']/(10**9),
            alpha=0.7,edgecolors="k",linewidth=1.5, cmap='RdYlGn')
plt.ylim(20,85)
plt.xlabel('Population In Billion')
plt.ylabel('Life Expetency')
plt.title('Population V/s Life Expectency', fontsize=14)
plt.yscale('log')
plt.colorbar()
plt.grid(True)
plt.show()

""" ######################################################################### """
""" ########################### VOLATALITY PLOTS ############################ """
""" ######################################################################### """
daily_stock_data = pd.read_csv("11_Daily Stock.csv", index_col=0, parse_dates=True, 
                               na_values='.',infer_datetime_format=True,squeeze=True).dropna()
state = pd.cut(daily_stock_data, bins=[-np.inf, 14, 18, 24, np.inf],labels=range(4))

""" Plotting A Series """
daily_stock_data.plot(marker='',color='k',linewidth=1,
                      figsize=(15,4),label='Daily Stock Price')
ax = plt.gca()
ax.set_xlabel('Dates')
ax.set_ylabel('Stock Price In USD')
ax.set_title('Volatility Regime State')
ax.grid(False)
ax.legend(loc='lower right')
ax.axhline(daily_stock_data.mean(), linestyle='dashed', color='xkcd:dark grey',
           alpha=0.6,marker='')

trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
cmap = plt.get_cmap('RdYlGn_r')
for i, color in enumerate(cmap([0.2, 0.4, 0.6, 0.8])):
    ax.fill_between(daily_stock_data.index, 0, 1, where=state==i,
                    facecolor=color, transform=trans)

""" ######################################################################### """
""" ############################## BOX PLOTS ################################ """
""" ######################################################################### """
iris  = pd.read_csv("11_Iris.csv")
iris['species']=pd.Categorical(iris['species'])

""" Box Plot """
sns.boxplot(x='species', y='sepal_length', data=iris,
            order=["Virginica", "Versicolor", "Setosa"])
sns.stripplot(x='species', y='sepal_length', 
              data=iris,order=["Virginica", "Versicolor", "Setosa"],
              color="orange", jitter=0.2, size=3)
plt.xlabel("")
plt.ylabel("Sepal Length")
plt.title("Species V/s Sepal Length")
plt.show()

""" Violin Plot """
sns.violinplot(x='species', y='petal_length', data=iris,
               order=["Virginica", "Versicolor", "Setosa"])
sns.stripplot(x='species', y='petal_length', 
              data=iris,order=["Virginica", "Versicolor", "Setosa"],
              color="orange", jitter=0.2, size=3)
plt.xlabel("")
plt.ylabel("Petal Length")
plt.title("Species V/s Petal Length")
plt.show()

""" Box Plot With Number of Obeservation"""
medians = iris.groupby(['species'])['sepal_length'].median().values
nobs = iris.groupby("species").size().values
nobs = [str(x) for x in nobs.tolist()]
nobs = ["n: " + i for i in nobs]

sns.boxplot(x='species', y='sepal_length', data=iris)
pos = range(len(nobs))
for tick,label in zip(pos,ax.get_xticklabels()):
    plt.text(pos[tick], medians[tick], nobs[tick], 
             horizontalalignment='center', size='medium', 
             color='k', weight='semibold')
 
plt.xlabel("")
plt.ylabel("Sepal Length")
plt.title("Species V/s Sepal Length")
plt.show()

""" ######################################################################### """
""" ######################### CORRELATION PLOTS ############################# """
""" ######################################################################### """

""" For All Variables """
sns.pairplot(iris,dropna  = True,
             kind="scatter",markers=["o", "s", "D"], palette="Set2", 
             hue="species",hue_order =["Virginica", "Versicolor", "Setosa"])

""" For Selected Variables """
sns.pairplot(iris,vars=["sepal_width", "sepal_length"],dropna  = True,
             kind="scatter",markers=["o", "s", "D"], palette="Set2", 
             hue="species",hue_order =["Virginica", "Versicolor", "Setosa"])

""" Setting X & Y Variables  """
sns.pairplot(iris,dropna  = True,
             x_vars=["sepal_width", "sepal_length"],
             y_vars=["petal_width", "petal_length"],
             kind="scatter",palette="Set2")

""" Regression Plot """
sns.pairplot(iris,dropna  = True,kind="reg",diag_kind= "kde",palette="Set2")

""" ######################################################################### """
""" ############################## BAR PLOTS ################################ """
""" ######################################################################### """
continents = pd.read_csv("11_Continent.csv")

""" Bar Plots """
x_pos = np.arange(5) 
bar_width = 0.35
p1 = plt.bar(x_pos, continents['Men_Mean'], bar_width, yerr=continents['Men_Std'])
p2 = plt.bar(x_pos+bar_width, continents['Women_Mean'],bar_width, yerr=continents['Women_Std'])
plt.legend((p1[0], p2[0]), ('Men', 'Women'))
plt.ylabel('Scores')
plt.xticks(x_pos+bar_width/ 2, continents['continent'])
plt.title('Test Scores Across Continents')
plt.tight_layout()
plt.show()

""" Bar Plots With Secondary Axis """
fig = plt.figure()

ax1 = fig.add_subplot(121) 
ax2 = ax1.twinx()
continents.Men_Mean.plot(kind='bar',color='red', ax=ax1, width=0.4, position=1)
continents.Men_Std.plot(kind='bar',color='green', ax=ax2, width=0.4, position=0)
ax1.set_ylabel('Score Mean')
ax2.set_ylabel('Std Mean')
plt.xticks([0,1,2,3,4], continents['continent'])
plt.grid(False)
plt.show()

""" Stcked Bar Plots """
p1 = plt.bar(continents['continent'], continents['Men_Mean'], yerr=continents['Men_Std'])
p2 = plt.bar(continents['continent'], continents['Women_Mean'], yerr=continents['Women_Std'],
             bottom = continents['Men_Mean'])
plt.legend((p1[0], p2[0]), ('Men', 'Women'))
plt.ylabel('Scores')
plt.title('Test Scores Across Continents')
plt.tight_layout()
plt.show()

""" ######################################################################### """
""" ################################# HISTOGRAMS ############################ """
""" ######################################################################### """
mu = 0
sigma = 1
bins = 20
x = np.random.normal(mu, sigma, 3000)

fig, ax1 = plt.subplots()
n, bins, patches = ax1.hist(x, bins, density = False,cumulative = False,
                            histtype='bar', edgecolor='k', align = "mid",
                            orientation = "vertical",facecolor='green', alpha=0.5)
ax1.set_xlabel('Bins')
ax1.set_ylabel('Frequencies')

ax2 = ax1.twinx()
y = mlab.normpdf(bins, mu, sigma)
ax2.plot(bins,y, 'r--')
ax2.set_ylabel('Probabilies')

plt.title('Histogram $\mu=0$, $\sigma=1$',fontsize=12)
fig.tight_layout()
fig.show()

""" ######################################################################### """
""" ############################# READING IMAGE FILES ####################### """
""" ######################################################################### """

""" Grayscale Images: (M, N), RGB Images : (M, N, 3), RGBA Images: (M, N, 4) """
img = plt.imread('11_Sunflower.jpg')
print(img.shape)

plt.imshow(img)
plt.axis('off')
plt.show()

""" Converting RGB Image To Grayscale """
collapsed = img.mean(axis=2)
print(collapsed.shape)
plt.imshow(collapsed)
plt.axis('off')
plt.show()


plt.imshow(collapsed,interpolation = 'bicubic' )
plt.axis('off')
plt.show()


collapsed = img.mean(axis=2)
print(collapsed.shape)
plt.imshow(collapsed[::4,::4], cmap='gray', aspect = 1.0, extent= (0,1024,0,1024))
plt.axis('off')
plt.show()
