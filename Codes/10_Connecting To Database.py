""" ######################################################################### """
""" ################### Connecting To Database In Python #################### """
""" ######################################################################### """
import numpy as np
import pandas as pd
import os
home_dir = "C:/Users/debas/Downloads/Python Code Library/Numpy, Pandas, Matplotlib, Bokeh/Datasets"
os.chdir(home_dir)

""" ############################# """
""" #### Importing SQLITE Files   """
""" ############################# """

""" Creating SQLITE Engine """
from sqlalchemy import create_engine
engine = create_engine('sqlite:///10_SQLITE_File.sqlite')
""" engine = create_engine('postgresql://user:password@host:port/database_name') """
print(list(engine.table_names()))

""" Runing SQL Query Through Pandas """
df_census = pd.read_sql_query("SELECT * FROM census", engine)
df_state = pd.read_sql_query("SELECT * FROM state_fact", engine)

""" Runing SQL Query On Connection Object """
with engine.connect() as connection:
    resultset_1 = connection.execute("SELECT * FROM census")
    df_census = pd.DataFrame(resultset_1.fetchall())
    df_census.columns = resultset_1.keys()
    
    resultset_2 = connection.execute("SELECT * FROM state_fact")
    df_state = pd.DataFrame(resultset_2.fetchmany(5))
    df_state.columns = resultset_2.keys()
    
    connection.close()
    
""" SQL Quering Through Metadata  """
from sqlalchemy import MetaData, Table, select, desc
connection = engine.connect()
metadata_census = Table('census', MetaData(), autoload=True,autoload_with=engine)
metadata_state_fact = Table('state_fact', MetaData(), autoload=True,autoload_with=engine)
print(repr(metadata_census)) 
print(repr(metadata_state_fact)) 

stmt = select([metadata_census])

""" Where Clause (<=, >=, != >, < Acceptable) """
stmt_1 = stmt.where(metadata_census.columns.state == 'California')
rs_1 = pd.DataFrame(connection.execute(stmt_1).fetchall())

stmt_2 = stmt.where(metadata_census.columns.state.startswith('New'))
rs_2 = pd.DataFrame(connection.execute(stmt_2).fetchall())

""" AND, OR, NOT In Where Clause """
from sqlalchemy import and_, or_, not_
stmt_3 = stmt.where(or_(metadata_census.columns.state == 'California',
                        metadata_census.columns.state == 'New York'))
rs_3 = pd.DataFrame(connection.execute(stmt_3).fetchall())

stmt_4 = stmt.where(not_(metadata_census.columns.sex=='M'))
rs_4 = pd.DataFrame(connection.execute(stmt_4).fetchall())

""" Ordering Query Result """
stmt_5 = stmt.order_by(desc(metadata_census.columns.state),metadata_census.columns.sex)
rs_5 = pd.DataFrame(connection.execute(stmt_5).fetchall())

""" Aggregate Functions (Avg, Count, Min, Max, Sum) """
from sqlalchemy import func
stmt_6 = select([func.sum(metadata_census.columns.pop2008)])
rs_6 = connection.execute(stmt_6).scalar()

""" Group By """
stmt_7 = select([metadata_census.columns.state,
                 metadata_census.columns.sex,
                 func.sum(metadata_census.columns.pop2000),
                 func.sum(metadata_census.columns.pop2008)])
stmt_7 = stmt_7.group_by(metadata_census.columns.state,metadata_census.columns.sex)
rs_7= pd.DataFrame(connection.execute(stmt_7).fetchall())

stmt_8 = select([metadata_census.columns.age,
                func.avg(metadata_census.columns.pop2008-metadata_census.columns.pop2000)])
stmt_8 = stmt_8.group_by(metadata_census.columns.age)
rs_8= pd.DataFrame(connection.execute(stmt_8).fetchall())

""" Case Statements """
from sqlalchemy import case
stmt_9 = select([
        func.sum(
                case([
                        (metadata_census.columns.state=="New York",
                         metadata_census.columns.pop2008)],
                         else_=0))])
rs_9 = connection.execute(stmt_9).scalar()

from sqlalchemy import case, cast, Float
stmt_10 = select([
        (func.sum(
                case([
                        (metadata_census.columns.state=="New York",
                         metadata_census.columns.pop2008)],
                         else_=0))/
                        cast(func.sum(metadata_census.columns.pop2008),Float)*100)])
rs_10 = connection.execute(stmt_10).scalar()

"""" Automatic Join """
stmt_11 = select([metadata_census.columns.pop2008,metadata_state_fact.columns.abbreviation])
rs_11 = pd.DataFrame(connection.execute(stmt_11).fetchall())

""" Joins """
stmt_12 = select([func.sum(metadata_census.columns.pop2000)])
stmt_12 = stmt_12.select_from(metadata_census.join(metadata_state_fact,metadata_state_fact.columns.name
                                                   == metadata_census.columns.state))
stmt_12 = stmt_12.where(metadata_state_fact.columns.census_division_name=="East South Central")
rs_12 = connection.execute(stmt_12).scalar()

stmt_13 = select([func.sum(metadata_census.columns.pop2000)])
stmt_13 = stmt_13.select_from(metadata_census.join(metadata_state_fact,metadata_state_fact.columns.name
                                                   == metadata_census.columns.state))
stmt_13 = stmt_13.where(metadata_state_fact.columns.circuit_court=='10')
rs_13 = connection.execute(stmt_13).scalar()
