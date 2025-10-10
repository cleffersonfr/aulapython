import pandas as pd
import openpyxl
import streamlit as st



uploaded = st.file_uploader('Fazer upload'
                  )

if uploaded is not None:
    df_upload = pd.read_excel(uploaded,sheet_name="Base",header=2)
    

    df_index  = pd.read_excel(uploaded,sheet_name="Index")

    df_upload = df_upload.drop(columns=['Region','State','Legal Entity','Legal Entity Name',
                        'BU','BU Name','IBX','Parent Cost Center','Intercompany','Product','Future1','Account Distribution',
                        'Ledger Name','Je Header ID','Je Line Num','Journal Source','Journal Category','Journal Name',
                        'Batch Name','Batch Created By','Journal Line Description','FAH Event Type','Functional Currency Code',
                        'Functional Currency Code','EBS Transaction Number','Sales Order Number','PO Category','PO Line Description',
                        'Commodity Code','Purpose Of Purchase','Project Reference','Parent Name','Journal Posted By',
                        'Customer Reference 1','Customer Reference 3','Asset Number','Asset Category','Asset Location',
                        'Asset Description','UUID','Source File Name','EBS Journal Line Description'],errors='ignore',axis=1)
    
    #df_upload = df_upload.drop(columns=colunas_remover, errors='ignore')

    df_index['Account'] = df_index['Account'].astype('Int64')
    df_upload['Account'] = df_upload['Account'].astype('Int64')

    df_index['Account'] = df_index['Account'].astype('Int64')
    df_upload = pd.merge(df_upload, df_index[['Account','Agrupamento']], on='Account',how='left')

    df_upload['Period Name'] = pd.to_datetime(df_upload['Period Name'],format='%b-%y')
    df_upload['Year'] = df_upload['Period Name'].dt.year
    df_upload['Month'] = df_upload['Period Name'].dt.month

    df_upload.to_excel('relatorio_tratado.xlsx')

    df_upload = df_upload[df_upload['Year']==2025]
    df_agrupado_mes_conta = df_upload.groupby(['Agrupamento', 'Month'])['Functional Net'].sum() / 1000

    st.set_page_config(layout="wide")

    st.title('Análise de despesas - Carreta Furacão 💵 ')

    st.subheader('Sintético por mês')
    pivot = df_upload.pivot_table(values='Functional Net', index='Agrupamento', columns='Month', aggfunc='sum', fill_value=0)
    st.dataframe(pivot.style.format("$ {:,.0f}"))

    total_por_mes = pivot.sum(axis=0)  # Soma todos os agrupamentos
    st.bar_chart(total_por_mes)


