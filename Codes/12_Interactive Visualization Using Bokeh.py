import numpy as np
import pandas as pd
import os
os.chdir("C:/Users/debas/Downloads/Python Code Library/Numpy, Pandas, Matplotlib, Bokeh/Datasets")

""" ######################################################################### """
""" ########################### BASIC INTERACTIVITY ######################### """
""" ######################################################################### """

""" Scattered Plot (Zoom Facility) """
literacy_data = pd.read_csv("12_Literacy Birth Rate.csv")
lat_data = literacy_data.loc[literacy_data['Continent']=='LAT',:]
afr_data = literacy_data.loc[literacy_data['Continent']=='AF',:]
asi_data = literacy_data.loc[literacy_data['Continent']=='ASI',:]
eur_data = literacy_data.loc[literacy_data['Continent']=='EUR',:]

from bokeh.plotting import figure
from bokeh.io import output_file, show
plot = figure(x_axis_label='fertility (children per woman)', y_axis_label ='female_literacy (% population)')
plot.circle(lat_data['fertility'], lat_data['female literacy'], color='blue', size=10, alpha=0.8)
plot.x(afr_data['fertility'], afr_data['female literacy'], color='blue', size=10, alpha=0.8)
output_file('Plot.html')
show(plot)

""" Line Plot (Zoom Facility) """
daily_stock_data = pd.read_csv("12_Apple Stock.csv")
daily_stock_data['date'] = pd.to_datetime(daily_stock_data.date, format='%d-%m-%Y')

from bokeh.plotting import figure
from bokeh.io import output_file, show
plot = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')
plot.line(daily_stock_data['date'], daily_stock_data['adj_close'])
output_file('Plot.html')
show(plot)

""" Line Plot With Marker (Zoom Facility) """
from bokeh.plotting import figure
from bokeh.io import output_file, show
plot = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')
plot.circle(daily_stock_data['date'], daily_stock_data['adj_close'], fill_color='white', size=4)
plot.line(daily_stock_data['date'], daily_stock_data['adj_close'])
output_file('Plot.html')
show(plot)

""" ######################################################################### """
""" ############################# SELECTION TOOLS ########################### """
""" ######################################################################### """
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource

olympic_data = pd.read_csv("12_Sprint.csv")
source = ColumnDataSource(olympic_data)
plot = figure(x_axis_label='Year', y_axis_label='Time',tools='box_select,lasso_select')
plot.circle(x='Year', y='Time', source=source, 
            selection_color='red', nonselection_fill_alpha=0.2,nonselection_fill_color='grey')
output_file('Plot.html')
show(plot)

""" ######################################################################### """
""" ############################### HOVER TOOLS ############################# """
""" ######################################################################### """
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.plotting import ColumnDataSource

glucose_data = pd.read_csv("12_Glucose.csv", parse_dates=True)
glucose_data['datetime'] = pd.to_datetime(glucose_data.datetime)
source = ColumnDataSource(glucose_data)

plot = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='Glucose Level')
plot.circle(x='datetime', y='glucose', source = source, size=10,
         fill_color='blue', alpha=0.5, line_color=None,
         hover_fill_color='red', hover_alpha=0.8,
         hover_line_color='white')
hover = HoverTool(tooltips=[('ISIG','@isig'),('Glucose','@glucose')])
plot.add_tools(hover)
output_file('Plot.html')
show(plot)

""" ######################################################################### """
""" ############################### COLOR MAPPING ########################### """
""" ######################################################################### """
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.models import CategoricalColorMapper

auto_data = pd.read_csv("12_Auto Data.csv")
source = ColumnDataSource(auto_data)
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'], palette=['red', 'green', 'blue'])
plot = figure()
plot.circle('weight', 'mpg', source=source,
            color=dict(field='origin', transform=color_mapper),legend='origin')
output_file('Plot.html')
show(plot)

""" ######################################################################### """
""" ################### SIMPLE LAYOUTS (NO COMMON SCALING) ################## """
""" ######################################################################### """
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.layouts import row, column
from bokeh.models import HoverTool

literacy_data = pd.read_csv("12_Literacy Birth Rate.csv")
lat_data = literacy_data.loc[literacy_data['Continent']=='LAT',:]
afr_data = literacy_data.loc[literacy_data['Continent']=='AF',:]
asi_data = literacy_data.loc[literacy_data['Continent']=='ASI',:]
eur_data = literacy_data.loc[literacy_data['Continent']=='EUR',:]

p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p1.circle('fertility', 'female literacy', source= ColumnDataSource(lat_data), legend='Latin America')

p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p2.circle('fertility', 'female literacy', source= ColumnDataSource(afr_data), legend='Africa')

p3 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p3.circle('fertility', 'female literacy', source= ColumnDataSource(asi_data), legend='Asia')

p4 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p4.circle('fertility', 'female literacy', source= ColumnDataSource(eur_data), legend='Europe')

layout_1 = row(column(p1,p3),column(p2,p4))
output_file('Plot.html')
show(layout_1)

""" ######################################################################### """
""" #################### GRID LAYOUTS (WITH COMMON SCALING) ################# """
""" ######################################################################### """
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.layouts import gridplot

literacy_data = pd.read_csv("12_Literacy Birth Rate.csv")
lat_data = literacy_data.loc[literacy_data['Continent']=='LAT',:]
afr_data = literacy_data.loc[literacy_data['Continent']=='AF',:]
asi_data = literacy_data.loc[literacy_data['Continent']=='ASI',:]
eur_data = literacy_data.loc[literacy_data['Continent']=='EUR',:]

p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p1.circle('fertility', 'female literacy', source= ColumnDataSource(lat_data), legend='Latin America')

p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p2.circle('fertility', 'female literacy', source= ColumnDataSource(afr_data), legend='Africa')

p3 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p3.circle('fertility', 'female literacy', source= ColumnDataSource(asi_data), legend='Asia')

p4 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p4.circle('fertility', 'female literacy', source= ColumnDataSource(eur_data), legend='Europe')

p4.y_range = p3.y_range = p2.y_range = p1.y_range
p4.x_range = p3.x_range = p2.x_range = p1.x_range

layout_2 = gridplot([[p1,p3],[p2,p4]])
output_file('Plot.html')
show(layout_2)

""" ######################################################################### """
""" ############################## TAB LAYOUTS ############################## """
""" ######################################################################### """
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs

literacy_data = pd.read_csv("12_Literacy Birth Rate.csv")
lat_data = literacy_data.loc[literacy_data['Continent']=='LAT',:]
afr_data = literacy_data.loc[literacy_data['Continent']=='AF',:]
asi_data = literacy_data.loc[literacy_data['Continent']=='ASI',:]
eur_data = literacy_data.loc[literacy_data['Continent']=='EUR',:]

p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p1.circle('fertility', 'female literacy', source= ColumnDataSource(lat_data), legend='Latin America')

p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p2.circle('fertility', 'female literacy', source= ColumnDataSource(afr_data), legend='Africa')

p3 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p3.circle('fertility', 'female literacy', source= ColumnDataSource(asi_data), legend='Asia')

p4 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p4.circle('fertility', 'female literacy', source= ColumnDataSource(eur_data), legend='Europe')

""" Tab Layout """
tab1 = Panel(child=p1, title='Latin America')
tab2 = Panel(child=p2, title='Africa')
tab3 = Panel(child=p3, title='Asia')
tab4 = Panel(child=p4, title='Europe')
layout_3 = Tabs(tabs=[tab1, tab2, tab3, tab4])
output_file('Plot.html')
show(layout_3)