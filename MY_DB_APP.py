import streamlit as st
import pandas as pd
import requests
import numpy as np
from urllib.error import URLError
from snowflake.snowpark import Session
import snowflake.snowpark as snowpark 

st.title('SNOWFLAKE DASHBOARDS')
st.write("Here's our first attempt at using data to create a table:")
df=st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

connection_parameters = {
    "account": "wu00137.central-india.azure",
    "user": "sashanth",
    "password": "Alpha123@",
    "role": "ACCOUNTADMIN",  
    "warehouse": "COMPUTE_WH", 
    "database": "S_T_VALIDATION", 
    "schema": "Test", 
 }  

new_session = Session.builder.configs(connection_parameters).create()
tableName = 'S_T_VALIDATION.Test.MAPPING_TABLE'
df_table = new_session.table(tableName)
df=df_table.to_pandas()
