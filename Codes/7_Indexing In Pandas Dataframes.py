""" ###################################################################################### """
""" ########################### INDEXING IN PANDAS DATAFRAMES  ########################### """
""" ###################################################################################### """
import pandas as pd
import numpy as np
import os
os.getcwd()
os.chdir("C:/Users/debas/Downloads/Python Code Library/Numpy, Pandas, Matplotlib, Bokeh/Datasets")

weather = pd.read_csv('7_Pittsburgh_2013.csv',index_col='Date', parse_dates=True)
week1_range = weather.loc['2013-07-01':'2013-07-07',['Min TemperatureF', 'Max TemperatureF']]
week1_mean = weather.loc['2013-07-01':'2013-07-07','Mean TemperatureF']
week1_range.divide(week1_mean, axis='rows')
week1_mean.pct_change() * 100

""" Arithmatic Operations Using Indexing """
bronze = pd.read_csv('7_Medals_Bronze.csv', index_col=0)
silver = pd.read_csv('7_Medals_Silver.csv', index_col=0)
gold = pd.read_csv('7_Medals_Gold.csv', index_col=0)
total_medals = bronze.add(silver, fill_value=0).add(gold, fill_value=0)

""" ###################################################################################### """
""" ##################### HIERARCHICAL INDEXING IN PANDAS DATAFRAMES  #################### """
""" ###################################################################################### """

stocks = pd.read_csv('7_Stocks.csv')
stocks['Date'] = pd.to_datetime(stocks['Date'])
print(stocks)

""" Hierarchical Indexing is like setting composit key in Pandas Dataframe """
stocks = stocks.set_index(['Symbol','Date'])
stocks = stocks.sort_index()
print(stocks)
print(type(stocks.index))                               """ Multi Index """
print(stocks.index)

unstacked_df = stocks.unstack(level='Symbol')           """ Unstacking Based On A Column """
print(unstacked_df)
stacked_df = unstacked_df.stack(level='Symbol')         """ Stacking Based On A Column """
print(stacked_df)
swapped_df = stocks.swaplevel(0, 1).sort_index()        """ Swapping Index Levels """
print(swapped_df)

""" Slicing Outermost Index """"
stocks.loc['AAPL']                                      """ Single Index """
stocks.loc['CSCO':'MSFT']                               """ Range Index """
stocks.loc[['AAPL', 'MSFT']]                            """ Disjoint Index """

""" Slicing Outer & Inner Index """
stocks.loc['AAPL','2016-10-05']                         """ Single Composit Index """
stocks.loc[(['AAPL', 'MSFT'], '2016-10-05'), :]         """ Multiple Composit Index """
stocks.loc[('CSCO', ['2016-10-05', '2016-10-03']), 'Close']
stocks.loc[(['AAPL', 'MSFT'], ['2016-10-05', '2016-10-03']), 'Volume']  

""" Slicing Innermost Index """"
stocks.loc[(slice(None),'2016-10-05'),:]                """ Single Index """
stocks.loc[(slice(None),['2016-10-03','2016-10-05']),:] """ Multiple Index """

""" Appending Using Indecies """
rain2013 = pd.read_csv("7_Rainfall_2013.csv", index_col='Month', parse_dates=True)
rain2014 = pd.read_csv("7_Rainfall_2014.csv", index_col='Month', parse_dates=True)
pd.concat([rain2013, rain2014], axis=0)
pd.concat([rain2013, rain2014], keys=[2013, 2014], axis=0)
pd.concat([rain2013, rain2014], axis=1)
pd.concat([rain2013, rain2014], keys=[2013, 2014], axis=1)