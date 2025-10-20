import pandas as pd
import streamlit as st
from io import StringIO


data_atual = pd.Timestamp.now()

col1, col2, col3 = st.columns([1,3,1])

with col2:
    st.title('Open PO Analysis 📰')



uploaded_file = st.file_uploader('Importar extração do Open PO')



if uploaded_file is not None:
    openpo = pd.read_excel(uploaded_file,
                      usecols=['BU Country','Location','Location Description','Cost Center Description',
                       'GL Account Description','PO #','PO Line #','PO Creation Date in Source System',
                       'PO Status','PO Line Status','Supplier #','Supplier Name',
                       'GL Project Description','Need by Date','Ordered Amount (Reporting Currency)',
                       'Remaining Amount (Reporting Currency)'])
    
     #Formatar need by date para data
    openpo['Need by Date Formatado'] = openpo['Need by Date'].dt.strftime('%b-%Y')
    #filtrar apenas PO Linhas Abertas

    openpo = openpo[openpo['PO Line Status'] == "OPEN"]

    #filtrar apenas PO com remaining amount > 0
    openpo = openpo[openpo['Remaining Amount (Reporting Currency)'] > 0]

    #==================================================================================================================================================================
    #criar tipos de gastos para poder fazer os filtros 
    openpo['tipo_gasto'] = 'Outros'
    openpo.loc[openpo['GL Project Description'].isin(['0000 - DEFAULT PROJECT','8069 - OPEX ACCELERATION']),'tipo_gasto'] = 'Opex'
    openpo.loc[openpo['GL Project Description'].isin(['8001 - NATIONAL MAINT','8000 - CORRECTIVE MAINTENANCE','8002 - PREVENTIVE MAINT']),'tipo_gasto'] = 'R&M'
    openpo.loc[openpo['GL Project Description'].isin(['5300 - INFRA SPOF','5200 - MAINT-GENERAL']),'tipo_gasto'] = 'Controllable Capex'
    openpo.loc[openpo['GL Project Description'].isin(['3990 - INITIAL INSTALLATION','5100 - RECONFIG INSTALL']),'tipo_gasto'] = 'Success Based Capex'
    openpo['Need by Date'] = pd.to_datetime(openpo['Need by Date'])
    #================================================================================================================================================================== 
    
    #criar um datadrame que vai ser impactado plos filtros e que vai enviar os dados filtrados para o streamlit
    dataframe_filtrado = openpo.copy()
    
    
else:
    st.subheader('Nenhum arquivo disponível')



#===================================================================================================================
#LISTAS DE VALORES PARA CRIAR FILTROS
#==================================================================================================================
lista_paises = openpo['BU Country'].unique()
lista_tipo_gasto = openpo['tipo_gasto'].unique()
lista_site = dataframe_filtrado['Location Description'].unique()
#==================================================================================================================


#====================================================================================================================
#SIDEBAR
#=====================================================================================================================
with st.sidebar:
    st.subheader('Aplicar os filtros abaixo:')

    data_corte = st.date_input('Inserir a data atual')
    if data_corte:
        data_corte = pd.Timestamp(data_corte)
        dataframe_filtrado = dataframe_filtrado[dataframe_filtrado['Need by Date']<=data_corte]


    pais_selecionado = st.multiselect('Selecionar país:',lista_paises)
    if pais_selecionado:
        dataframe_filtrado = dataframe_filtrado[dataframe_filtrado['BU Country'].isin(pais_selecionado)]
        lista_site = dataframe_filtrado['Location Description'].unique()
        
        
    else:
        lista_site = openpo['Location Description'].unique()
        

    site_selecionado = st.multiselect('Selecionar IBX:',lista_site)
    if site_selecionado:
        dataframe_filtrado = dataframe_filtrado[dataframe_filtrado['Location Description'].isin(site_selecionado)]
    
    gasto_selecionado = st.selectbox('Tipo de Gasto',lista_tipo_gasto)
    if gasto_selecionado:
        dataframe_filtrado = dataframe_filtrado[dataframe_filtrado['tipo_gasto'] == (gasto_selecionado)]
    
    
    st.image('https://media1.tenor.com/m/vCdo4GQSxVkAAAAd/fiesta-superheros-capitan-am%C3%A9rica.gif')
    st.text('Created by Xis Frizzo')
                    
                                            
#====================================================================================================================
#FORMATAÇÃO DAS COLUNAS E INFORMAÇÕES PARA O GRÁFICO E PARA O DATAFRAME
#=====================================================================================================================

if pais_selecionado: #se for selecionado algum país no filtro o gráfico e o subheader mudam para detalhe por IBX
    grafico = dataframe_filtrado.groupby('Location Description')['Remaining Amount (Reporting Currency)'].sum()

else:
    grafico = dataframe_filtrado.groupby('BU Country')['Remaining Amount (Reporting Currency)'].sum()

if pais_selecionado:
    st.subheader('📈 Resumo por IBX')
else:
    st.subheader('📈 Resumo por Pais')


st.bar_chart(grafico)



st.subheader('📝 Para ver os principais detalhes por PO, selecione o "checkbox" abaixo.')

#==================================================================================================================
# criar lista com as colunas que deverão aparecer no dataframe streamlit
colunas_mostrar_po_fornecedor = ['Location Description',
                       'PO #','PO Line #','Supplier Name',
                       'Need by Date Formatado','Ordered Amount (Reporting Currency)',
                       'Remaining Amount (Reporting Currency)']

#renomear as colunas para rótulos mais amigáveis
nome_colunas_ajustado = nomes_colunas = {
    'Location Description': 'Site',
    'Supplier Name': 'Fornecedor',
    'Need by Date Formatado': 'Need by Date',
    'Ordered Amount (Reporting Currency)': 'Valor Total',
    'Remaining Amount (Reporting Currency)': 'Valor Restante'
}
#==================================================================================================================
ver_dataframe = st.checkbox('Ver detalhe por Fornecedor e PO')


if ver_dataframe:
    df_exibir = dataframe_filtrado[colunas_mostrar_po_fornecedor].copy()
    df_exibir['Ordered Amount (Reporting Currency)'] = df_exibir['Ordered Amount (Reporting Currency)'].apply(lambda x: f'$ {x:,.1f}')
    df_exibir['Remaining Amount (Reporting Currency)'] = df_exibir['Remaining Amount (Reporting Currency)'].apply(lambda x: f'$ {x:,.1f}')
    st.dataframe(df_exibir[colunas_mostrar_po_fornecedor].rename(columns=nome_colunas_ajustado),hide_index=True,width=2000)
#Nesta última linha foi feito um rename das colunas, utilizando o nome antigo e o novo nome em um dicionário "nome coluna ajustado"
#==================================================================================================================