""" #################################################################################### """
""" ##################################### GLOBBING  #################################### """
""" #################################################################################### """
import numpy as np
import pandas as pd
import glob
import os
os.getcwd()
os.chdir("C:/Users/debas/Downloads/Python Code Library/Numpy, Pandas, Matplotlib, Bokeh/Datasets")
csv_files = glob.glob('7_Medals_*.csv')
print(csv_files)
list_data = []
for filename in csv_files:
    data= pd.read_csv(filename)
    list_data.append(data)

""" #################################################################################### """
""" ######################### MELTING DATA FRAMES (WIDE TO LONG)  ###################### """
""" #################################################################################### """
tb_df =  pd.read_csv("8_TB.csv")
melted_df = pd.melt(frame=tb_df,
                    id_vars=['country', 'year'],
                    var_name='metrics',
                    value_name='values')

""" #################################################################################### """
""" ############################## PIVOT TABLES (LONG TO WIDE)  ######################## """
""" #################################################################################### """
titanic = pd.read_csv("8_Titanic.csv")
titanic.head()
titanic.columns

""" Rows=index, columns=columns, values=1st arg; Values Must Be Numeric, Default Function Is Mean """
x1 = titanic.pivot_table(index='sex', columns='pclass', values='age', aggfunc='median') 
x2 = titanic.pivot_table(index='sex', columns='pclass', aggfunc={'survived':'mean', 'fare': 'median'})
x3 = titanic.pivot_table(index='sex', columns='pclass', values = 'survived', margins=True, fill_value=0)

""" Binning """                                                            
age_binned = pd.cut(titanic['age'], [0, 20, 40, 60, 80])
x4 = titanic.pivot_table(index=['sex', age_binned], columns='pclass', values ='survived').fillna(0)

fare_binned = pd.cut(titanic['fare'],4)
x5 = titanic.pivot_table(index=['sex', age_binned], 
                         columns=['pclass',fare_binned], 
                         values ='survived', ).fillna(0)

""" #################################################################################### """
""" ####################################### MERGING  ################################### """
""" #################################################################################### """

""" Appending (Vertical Stacking) Data Frames """
pop1 = pd.read_csv('8_Population1.csv', index_col=0)
pop2 = pd.read_csv('8_Population2.csv', index_col=0)
pop1.append(pop2)

population = pd.read_csv('8_Population0.csv',index_col=0)
unemployment = pd.read_csv('8_Unemployment.csv',index_col=0)
population.append(unemployment, ignore_index=False)

""" merge() is used to combine two or more dataframes on the basis of values of """
""" common columns or indices (usingleft_index=True or right_index=True).""" 
""" concat() is used to append one or more dataframes based on axis (row or column wise)."""
""" join() is used to merge teo dataframes on the basis of the index; """
""" instead of using merge() with the option left_index=True we can use join() """

pd.concat([population, unemployment], axis=0, join= "inner")
pd.concat([population, unemployment], axis=0, join= "outer")
pd.concat([population, unemployment], axis=1, join= "inner")
pd.concat([population, unemployment], axis=1, join= "outer")

bronze = pd.read_csv('8_Medals_Bronze.csv')
gold = pd.read_csv('8_Medals_Gold.csv')
pd.merge(bronze, gold, on=['NOC', 'Country'],suffixes=['_bronze', '_gold'], how='inner')
pd.merge(bronze, gold, on=['NOC', 'Country'],suffixes=['_bronze', '_gold'], how='outer')
pd.merge(bronze, gold, left_on=['NOC', 'Country'],right_on=['NOC', 'Country'],suffixes=['_bronze', '_gold'], 
         how='left')
pd.merge(bronze, gold, on=['NOC', 'Country'],suffixes=['_bronze', '_gold'], how='right')

bronze.set_index('NOC').join(gold.set_index('NOC'),lsuffix='_bronze', rsuffix='_gold',how='inner')
bronze.set_index('NOC').join(gold.set_index('NOC'),lsuffix='_bronze', rsuffix='_gold',how='outer')
bronze.set_index('NOC').join(gold.set_index('NOC'),lsuffix='_bronze', rsuffix='_gold',how='left')
bronze.set_index('NOC').join(gold.set_index('NOC'),lsuffix='_bronze', rsuffix='_gold',how='right')

""" Ordered Merging """
software = pd.read_csv('8_Hardware_Sales.csv', parse_dates=['Date']).sort_values('Date')
hardware = pd.read_csv('8_Software_Sales.csv', parse_dates=['Date']).sort_values('Date')
total = pd.merge_ordered(hardware, software, on=['Date', 'Company'],suffixes=['_hardware', '_software'])

""" #################################################################################### """
""" ################################### DATA AGGREGATION  ############################## """
""" #################################################################################### """

sales = pd.DataFrame({'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
                      'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
                      'bread': [139, 237, 326, 456],
                      'butter': [20, 45, 70, 98]})

sales.groupby('weekday')[['bread','butter']].mean()
sales.groupby('weekday')[['bread','butter']].sum()
sales.groupby('city')[['bread','butter']].max()
sales.groupby('weekday').count()
sales.groupby(['city','weekday']).mean()
sales.groupby('city')[['bread','butter']].agg(['max','sum'])
sales.groupby('city')[['bread', 'butter']].agg({'bread':'min', 'butter':'max'})

""" Aggregation Based On Foreign Key"""
customers = pd.Series(['Dave','Alice','Bob','Alice'])   
sales.groupby(customers)['bread'].sum()

""" Aggregation Based On Custom Functions """
sales.groupby('weekday')[['bread', 'butter']].agg(lambda x: x.max()-x.min()) 

""" transform Function Can Be Used To Create New Column """
sales['bread_avg'] = sales.groupby('city')['bread'].transform('mean')
sales['butter_avg'] = sales.groupby('weekday')['butter'].transform('mean')

""" #################################################################################### """
""" #################################### APPLY FUNCTION  ############################### """
""" #################################################################################### """
df =  pd.read_csv("8_Four Stocks.csv")

""" Passing Python Functions In Apply """
col_mean = df.iloc[:, 1:].apply(np.mean,axis=0)
row_mean = df.iloc[:, 1:].apply(np.mean,axis=1)

""" Passing User Defined Function In Apply """
def stock_avg(row):
  return (row['AAPL'] + row['IBM'] + row['CSCO'] + row['MSFT'])/4

df['Avg'] = df.apply(stock_avg, axis=1)