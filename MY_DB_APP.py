import streamlit as st
import pandas as pd
import requests
import numpy as np
from urllib.error import URLError

st.title('SNOWFLAKE DASHBOARDS')
st.write("Here's our first attempt at using Snowflake data to create a Dashboards:")

user_name = st.text_input('Snowflake User name', placeholder='Enter your SF username here',key=1)
password = st.text_input('Snowflake Password', placeholder='Enter your SF password here',key=2)
account = st.text_input('Snowflake Account Identifier ', placeholder='Enter your SF account identifier here',key=3)



conn = st.connection("snowflake")

	

conn.query("SHOW ROLES;")
df2 = conn.query('SELECT "name" as ROLES ,"assigned_to_users" as ASSIGNED_TO_USERS FROM TABLE(RESULT_SCAN(LAST_QUERY_ID())) WHERE "assigned_to_users" >= 1; ', ttl=600)

st.write(df2)
