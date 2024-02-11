import streamlit as st
import pandas as pd
import requests
import numpy as np
from urllib.error import URLError


user_name = st.text_input('Snowflake User name', placeholder='Enter your SF username here',key=1)
password = st.text_input('Snowflake Password', placeholder='Enter your SF password here',key=2)
account = st.text_input('Snowflake Account Identifier ', placeholder='Enter your SF account identifier here',key=3)



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
