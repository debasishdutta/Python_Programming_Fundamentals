""" ###################################################################################### """
""" ################################### PANDAS SERIES  ################################### """
""" ###################################################################################### """

""" Pandas Series is a 1-D indexed array like list. Numpy Array has implicitlly """ 
""" defined interger index but Pandas Series has explicitly defined index """

import numpy as np
import pandas as pd
                                                        
"""  Creating Series From Numpy Array or List """
sample_series = pd.Series([32,74,69,65],index=['dd','rkd','rdd','bd'])
print(sample_series)   
 
""" Creating Series From Dictionary """
sample_dict = {'DD' : 32, 'RKD' : 74, 'RDD' : 69, 'BD': 65}      
print(pd.Series(sample_dict))

""" Accessing Elements of Series """
print(sample_series.values)                 """ Values of The Series """
print(sample_series.index)                  """ Keys of The Series """
sample_series.index.name = "Names"          """ Adding Name To Series Index """
sample_series.index[2] = "rdd"              """ Not Possible; Immutable """
sample_series.index = sample_series.index.str.upper()
print(list(sample_series.items()))          """ Key-Value Pair of The Series """


print(sample_series['RDD'])                 """ Accessing Series With Key """
print(sample_series[['BD', 'RDD']])         """ Put [] While Accessing Multiple Elements """
print(sample_series['RKD':'BD'])            """ Range With Key """
print(sample_series[:2])                    """ First Two Elements """
print(sample_series[::2])                   """ Every Second Element Starting From 0 """
print(sample_series[1::2])                  """ Every Second Element Starting From 1 """


sample_series['DD'] = 30                    """ Updating """
sample_series['SK'] = 33                    """ Appending """
'Debasish Dutta' in sample_series           """ Key Searching """
sample_series[np.logical_and(sample_series>=30,sample_series <40)] """ Slicing """

""" Label Based & Integer Based Positioning In Pandas """
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
print(data)

print(data.loc[1])                          """ Label Based Positioning """
print(data.iloc[1])                         """ Integer Based Positioning """

print(data.loc[1:3])                        """ Values With Key 1 to 3 """   
print(data.iloc[1:3])                       """ Second and thord element from begining """

"""" Appending Pandas Series """"
northeast = pd.Series(['CT', 'ME', 'MA', 'NH', 'RI', 'VT','NJ', 'NY', 'PA'])
south = pd.Series(['DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA','DC', 'WV', 'AL', 'KY', 'MS', 'TN', 'AR', 'LA', 'OK', 'TX'])

new_series = northeast.append(south)
print(new_series.index)
new_series = northeast.append(south).reset_index(drop=True)
print(new_series.index)

new_series = pd.concat([northeast, south])
print(new_series.index)
new_series = pd.concat([northeast, south], ignore_index=True)
print(new_series.index)
