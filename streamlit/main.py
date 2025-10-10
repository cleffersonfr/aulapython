import streamlit as st 
import pandas as pd

df = pd.read_excel('./GL.xlsx')
print(df.head())

df.iloc[1]

