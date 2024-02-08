import streamlit as st
import pandas as pd
import requests
from urllib.error import URLError

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
