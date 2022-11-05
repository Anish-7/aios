import time
import streamlit as st
import pandas as pd
import sqlite3
import joblib

state= joblib.load('state.joblib')
con = sqlite3.connect("sysdata.db") 
# placeholder=st.empty()


one,two=st.columns(2)
 
data=pd.read_sql_query("SELECT * FROM sysdata", con)
pred_dat=data.iloc[:,1:4]
placeholder=st.empty()

with one:
    prediction=str(state.predict(pred_dat.tail(1)))
    stat=st.info(f'state -{prediction}')
    fig=st.line_chart(data.cpu0)
    fig=st.line_chart(data.cpu2)
    fig=st.line_chart(data.data_download)
    time.sleep(1)    


with two:

    fig=st.line_chart(data.cpu1)
    fig=st.line_chart(data.ram)
    fig=st.line_chart(data.data_upload)

    time.sleep(1)    

st.experimental_rerun()


         