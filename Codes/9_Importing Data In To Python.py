""" ######################################################################### """
""" ################### Importing Flat Files In To Python ################### """
""" ######################################################################### """
import numpy as np
import pandas as pd
import os
home_dir = "C:/Users/debas/Downloads/Python Code Library/Numpy, Pandas, Matplotlib, Bokeh/Datasets"
os.chdir(home_dir)

""" Importing CSV Files """
csv_file = pd.read_csv('9_CSV_File.csv', delimiter=';')
csv_file.shape
csv_file.head(5)
csv_file.columns
csv_file.describe()

""" Importing Tab Delimited Text Files """
tab_del_file = pd.read_csv('9_Tab_Delimited_Text_File.txt', delimiter='\t')
tab_del_file.shape
tab_del_file.head(5)
tab_del_file.columns
tab_del_file.describe()


""" Importing Excel (Xls Or Xlsx) Files """
excel_file = pd.ExcelFile('9_Excel_File.xlsx')

for i in range(len(excel_file.sheet_names)):
    if(i< len(excel_file.sheet_names)-1):
        excel_file_final = pd.merge(excel_file.parse(i), excel_file.parse(i+1), how='left')

excel_file_final.head(5)
excel_file_final.columns
excel_file_final.describe()

""" Importing SAS Files """
sas_file = pd.read_sas("9_SAS_File.SAS7BDAT")
sas_file.shape
sas_file.head(5)
sas_file.columns
sas_file.describe()

""" Importing STATA Files """
stata_file = pd.read_stata("9_Stata_File.dta")
stata_file.shape
stata_file.head(5)
stata_file.columns
stata_file.describe()

""" Importing HDF5 & MATLAB Files """
import h5py
hdf5_file = h5py.File( "9_HDF5_File.hdf5",'r+')
matlab_file = h5py.File("9_Matlab_File.mat")

list(hdf5_file.keys())      """ HDF5 File Is A Collection of Multiple Hierarchical Data Sets """
list(hdf5_file['meta'].keys())
hdf5_file['meta']['Duration'].value

list(hdf5_file['strain'].keys())
hdf5_file['strain']['Strain'].value

list(matlab_file.keys())
list(matlab_file['cjdata'].keys())
matlab_file['cjdata']['tumorBorder'].value

""" Importing A Web Page """
import requests
get_req = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
html_doc = get_req.text

""" BeautifulSoup Object Stores HTML Or XML Data In A Nested Structure """
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,  "html.parser")
print(soup.prettify())
print(soup.title.string)
print(soup.get_text())

for link in soup.find_all('a'):
    """ Extracting All URLs """
    print(link.get('href'))

""" Importing Files With No Headers """
col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'definite']
sunspots = pd.read_csv("9_Sunspot.csv", delimiter=';', header=None, names=col_names)
sunspots.info()

""" Replace -1 With NaN """
sunspots = pd.read_csv("9_Sunspot.csv", 
                       delimiter=';', 
                       header=None, 
                       names=col_names,
                       na_values='-1')

sunspots = pd.read_csv("9_Sunspot.csv", 
                       delimiter=';', 
                       header=None, 
                       names=col_names,
                       na_values={'sunspots':['-1']})

""" Create New Dates From Other Columns """
sunspots = pd.read_csv("9_Sunspot.csv", 
                       delimiter=';', 
                       header=None, 
                       names=col_names,
                       na_values={'sunspots':['-1']},
                       parse_dates=[[0, 1, 2]],
                       index_col=0)

""" Exporting Data """
sunspots.to_csv("Sunspots.csv")
sunspots.to_excel("Sunspots.xlsx")