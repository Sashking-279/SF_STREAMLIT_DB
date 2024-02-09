import streamlit as st
import pandas as pd
import requests
import numpy as np
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

conn = st.connection("snowflake")
df = conn.query("SELECT * from mapping_table;", ttl=600)
st.write(df)
# new_session = Session.builder.configs(connection_parameters).create()
# tableName = 'S_T_VALIDATION.Test.MAPPING_TABLE'
# df_table = new_session.table(tableName)
# df=df_table.to_pandas()

df = conn.query("SELECT user_name, COUNT(user_name) AS num_of_logins FROM snowflake.account_usage.login_history GROUP BY user_name")

# Create a bar chart
st.bar_chart(df, x="USER_NAME", y="NUM_OF_LOGINS")
