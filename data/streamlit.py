import time
import streamlit as st
import pandas as pd
import sqlite3

con = sqlite3.connect("data.db") 
# placeholder=st.empty()

# with placeholder.container():
    # cpu0,cpu1,cpu2,ram,data_download,data_upload=st.columns(6)  
one,two=st.columns(2) 
 
data=pd.read_sql_query("SELECT * FROM sysdata", con)
placeholder=st.empty()

with one:

    fig=st.line_chart(data.cpu0)
    fig=st.line_chart(data.cpu2)
    fig=st.line_chart(data.data_download)
    
    # st.write(fig)

    # st.empty()
    # st.dataframe(data)
    time.sleep(0.5)

with two:

    fig=st.line_chart(data.cpu1)
    fig=st.line_chart(data.ram)
    fig=st.line_chart(data.data_upload)
    
    # st.write(fig)

    # st.empty()
    # st.dataframe(data)
    time.sleep(0.5)    
    
    # with cpu2:

    #     fig=st.line_chart(data.cpu2)
    #         # st.write(fig)

    #     # st.empty()
    #     # st.dataframe(data)
    #     time.sleep(0.5)
    
    
    # with ram:

    #     fig=st.line_chart(data.ram)
    #         # st.write(fig)

    #     # st.empty()
    #     # st.dataframe(data)
    #     time.sleep(0.5)
    
    # with data_download:

    #     fig=st.line_chart(data.data_download)
    #         # st.write(fig)

    #     # st.empty()
    #     # st.dataframe(data)
    #     time.sleep(0.5)
    
    # with data_upload:

    #     fig=st.line_chart(data.data_upload)
    #         # st.write(fig)

    #     # st.empty()
    #     # st.dataframe(data)
    #     time.sleep(0.5)




    st.experimental_rerun()


         