import streamlit as st

from tabela_mestre import input_tabela_mestre

from apresentacao_resultado import mostra_tabela

df_actual, df_forecast, df_index = input_tabela_mestre()

col1, col2, col3 = st.columns([1,3,1])

with col2:
    st.title('Finance Dashboard')

# mostra_tabela(df_actual)
# mostra_tabela(df_forecast)


df_grafico = df_actual(['mes','USD'])
st.line_chart(df_grafico)