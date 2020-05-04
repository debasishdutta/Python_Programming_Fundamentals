""" ################################################################################## """
""" ############################### PANDAS DATAFRAMES  ############################### """
""" ################################################################################## """

import pandas as pd
import numpy as np
import os
os.getcwd()
os.chdir("C:/Users/debas/Downloads/Python Code Library/Numpy, Pandas, Matplotlib, Bokeh/Datasets")

""" Pandas Dataframes From Python Lists/ Tuples """
countries = ["Brazil", "Russia", "India", "China", "South Africa"]
capitals = ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"]
area = [8.516, 17.10, 3.286, 9.597, 1.221]
population = [200.4, 143.5, 1252, 1357, 52.98]
names = ("BR", "RU", "IN", "CH", "SA")
sample_df = pd.DataFrame({"Country" : countries,
                          "Capital": capitals, 
                          "Area": area, 
                          "Population": population},index=names)
print(sample_df)

""" Creating DataFrames Python Dictionary """
sample_dict = {"country":["Brazil", "Russia", "India", "China", "South Africa"],
               "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
               "area":[8.516, 17.10, 3.286, 9.597, 1.221],
               "population":[200.4, 143.5, 1252, 1357, 52.98]}
sample_df = pd.DataFrame(sample_dict,index=names)
print(sample_df)

""" Creating DataFrames From NumPy Array """
countries = np.array(["Brazil", "Russia", "India", "China", "South Africa"]).reshape(5,1)
capitals = np.array(["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"]).reshape(5,1)
area = np.array([8.516, 17.10, 3.286, 9.597, 1.221]).reshape(5,1)
population = np.array([200.4, 143.5, 1252, 1357, 52.98]).reshape(5,1)
sample_df = pd.DataFrame(np.concatenate([countries,capitals,area,population],axis=1),
                         columns=['Countries','Capitals', 'Area', 'Population'],
                         index=names)
print(sample_df)

""" Creating DataFrames From Pandas Series """
countries = pd.Series(["Brazil", "Russia", "India", "China", "South Africa"],index=names)
capitals = pd.Series(["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],index=names)
area = pd.Series([8.516, 17.10, 3.286, 9.597, 1.221],index=names)
population = pd.Series([200.4, 143.5, 1252, 1357, 52.98],index=names)
sample_df = pd.DataFrame({'Country': countries,'Capital': capitals, 
                          'Area': area, 'Population': population})
print(sample_df)

""" Accessing Elements of Pandas DataFrame """
print(sample_df.index)                      """ Keys """
sample_df.index.name = "Abbrevation"        """ Assigning Name To Row Index """
print(sample_df.columns)                    """ Column Names """
print(sample_df.values)                     """ Values """

""" Column Access With Lable Based Positioning  """
sample_df["Country"]                        """ Returns Country Column As Series """
sample_df.Country                           """ Returns Country Column As Series """
sample_df[["Country"]]                      """ Returns Country Column As Dataframe """
sample_df[["Country","Capital"]]            """ Returns Country and Capital Columns As Dataframe """

""" Row Access With Lable Based Positioning """
sample_df.loc["RU"]                         """ Returns Russia Row As Series """
sample_df.loc[["RU"]]                       """ Returns Russia Row As Dataframe """
sample_df.loc[["RU", "IN", "CH"]]           """ Returns Multiple Rows As Dataframe """

""" Row & Column Access With Lable Based Positioning """
sample_df.loc[["RU", "IN", "CH"], ["Country","Capital"]]
sample_df.loc[:, ["Country","Capital"]]

""" Row Access With Integer Based Index Positioning """
sample_df.iloc[1]                           """ Returns Second Row As Series """
sample_df.iloc[[1,2,3]]                     """ Returns Second, Third and Fourth Row As Dataframe """

""" Row & Column Access With Integer Based Index Positioning """
sample_df.iloc[[1,2,3], [0, 1]]
sample_df.iloc[:, [0, 1]]
sample_df.iloc[[1,2,3], :]

""" Accessing A Specific Value Within Dataframe """
sample_df['Capital']['IN']
sample_df.Capital['IN']

""" If you are using .loc or .iloc acceessor then format is """
""" [Row Names Or Row Number][Column Name Or Column Number] """
""" If you are directly accessing data frame then format is """
""" [Column Name][Row Name]. .loc can take boolean array as """
""" input index but .iloc can not take that """

""" Filtering & Slicing Pandas Data Frames """
sample_df[np.logical_and(sample_df.Area>3, sample_df.Area<10)]
sample_df.loc[np.logical_and(sample_df.Area>3, sample_df.Area<10),["Country","Capital"]]
sample_df.loc[np.logical_or(sample_df.Area>15, sample_df.Area<2),["Country","Capital"]]

""" Inspecting Pandas Dataframes """
sample_df.columns                           """ Column Names """
sample_df.shape                             """ Shape (Rows X Column) """
sample_df.info()                            """ Internal Structure """
sample_df.head(2)                           """ Top 2 Rows """
sample_df.tail(3)                           """ Bottom 3 Rows """

sample_df.Country.value_counts(dropna=False)""" Frequency Table of Country Column """
sample_df['Area'].value_counts(dropna=False)""" Frequency Table of Area Column """
sample_df.describe()                        """ Basic Statistics of Numeric Columns """

"""" Data Import """
df = pd.read_csv('6_Sales.csv', index_col='month')
df['bacon'] = [0, 0, 50, 60, 70, 80]
print(df)

""" Manipulating Dataframes """
df['spam'] = df['spam'].astype('int16')     """ Changing Data Type """
df.loc[:,df.all()]                          """ Select columns with all nonzeros """
df.loc[:,df.any()]                          """ Select columns with any nonzeros """
df.loc[:,df.isnull().any()]                 """ Select columns with any NaNs """
df.loc[:,df.notnull().all()]                """ Select columns without NaNs """
df.dropna(how='all')                        """ Drop rows with all NaNs """
df.dropna(how='any')                        """ Drop rows with any NaNs """
df.drop_duplicates()                        """ Drop Duplicates """
df.fillna(method='ffill')                   """ Forward Filling of Missing Value """
df.fillna(method='backfill')                """ Backward Filling of Missing Value """
df.eggs[df.salt>55] += 5                    """ Modifying a column based on another """
df.floordiv(12)                             """ Vectorized operation on Data Frame """
df['dozens_of_eggs'] = df.eggs.floordiv(12)
df.index = df.index.str.upper()