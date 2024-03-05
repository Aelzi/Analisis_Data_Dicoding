import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.dataframe_explorer import dataframe_explorer

# Fungsi untuk memuat data
df_hour=pd.read_csv("Bike-Sharing-dataset/hour.csv")
df_day=pd.read_csv("Bike-Sharing-dataset/day.csv")


def data_frame_hour(dataframe):
    
    st.markdown("## :green[Data Frame Hour ]")
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)
    
data_frame_hour(df_hour)

def data_frame_day(dataframe):
    
    st.markdown("## :blue[Data Frame Day ]")
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)
    
data_frame_day(df_day)