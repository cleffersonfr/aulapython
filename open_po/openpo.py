import pandas as pd
import streamlit as st


#carrega arquivo que está na pasta:
nome_arquivo = input('digite o nome do arquivo de acordo como salvou na pasta (sem ".xlsx"):' )
print(nome_arquivo)

#Limpa arquivo deixando apenas as colunas úteis
openpo = pd.read_excel(nome_arquivo +'.xlsx',
                      usecols=['BU Country','Location','Location Description','Cost Center Description',
                       'GL Account Description','PO #','PO Line #','PO Creation Date in Source System',
                       'PO Status','PO Line Status','Purpose of Purchase','Commodity Code','EBS PO Category',
                       'Supplier #','Supplier Name','GL Project Description','Need by Date','Ordered Amount (Reporting Currency)',
                       'Remaining Amount (Reporting Currency)']
                       
                                           
                      
                      )

#filtrar apenas PO Abertas
openpo = openpo[openpo['PO Line Status'] == "OPEN"]

#Cria um DF apenas de Opex
openpo_opex = openpo[
                        (openpo['GL Project Description'] == '0000 - DEFAULT PROJECT') |
                        (openpo['GL Project Description'] == '8069 - OPEX ACCELERATION')
]

#Cria um DF apenas de Capex (Projeto)
openpo_capex_projeto = openpo[
                        (openpo['GL Project Description'] == '5300 - INFRA SPOF') |
                        (openpo['GL Project Description'] == '5200 - MAINT-GENERAL')]

#Cria um DF apenas de R&M
openpo_rm = openpo[
                        (openpo['GL Project Description'] == '8001 - NATIONAL MAINT') |
                        (openpo['GL Project Description'] == '8000 - CORRECTIVE MAINTENANCE') |
                        (openpo['GL Project Description'] == '8002 - PREVENTIVE MAINT')

]

# Criar data frame de Opex por país como uma tabela dinâmica
openpo_opex_pais = openpo_opex.pivot_table(index='BU Country',
                                            columns=openpo_opex['Need by Date'].dt.year ,
                                            values='Remaining Amount (Reporting Currency)',
                                            aggfunc='sum'
                                            
                                         )




#penpo_opex_pais'Total Orderd']=openpo_opex_pais[e'otal Ordered'].apply(lambda x: f'$ {x:.1f}'.replace(',','.'))
#openpo_opex_pais['Total Remaining']=openpo_opex_pais['otal Remaining'].apply(lambda x: f'$ {x:.1f}ace(',','.'))

print(openpo_opex_pais.to_string(float_format='$ {:,.1f}'.format))

#Open PO por país e site:
openpo_opex_pais_site = openpo_opex.pivot_table(index=['BU Country','Location Description'],
                                                columns=openpo_opex['Need by Date'].dt.year,
                                                values='Remaining Amount (Reporting Currency)',
                                                aggfunc='sum')

print(openpo_opex_pais_site.to_string(float_format='$ {:,.1f}'.format))


#Open PO por país, site e conta contábil
openpo_country_site_account = openpo_opex.pivot_table(index=['BU Country','Location Description','GL Account Description'],
                                columns=openpo_opex['Need by Date'].dt.year,
                                values='Remaining Amount (Reporting Currency)',
                                aggfunc='sum')

print(openpo_country_site_account.to_string(float_format='$ {:,.1f}'.format))

#analítico por Site - Fornecedor - PO
open_po_analitico = openpo_opex.pivot_table(index=['BU Country','Location Description','Supplier Name','PO #'],
                                columns=openpo_opex['Need by Date'].dt.year,
                                values='Remaining Amount (Reporting Currency)',
                                aggfunc='sum')

print(open_po_analitico.to_string(float_format='$ {:,.1f}'.format))

with pd.ExcelWriter('OpenPO_Analysis.xlsx') as writer:
    openpo_opex_pais.to_excel(writer, sheet_name='Country')
    openpo_opex_pais_site.to_excel(writer, sheet_name='IBX')
    openpo_country_site_account.to_excel(writer, sheet_name='Account - IBX')
    open_po_analitico.to_excel(writer, sheet_name="Supplier_PO") 