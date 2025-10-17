import pandas as pd
import streamlit as st
from amortizacao import calcula_financiamento
from conversor import conversor



st.title('💵Calculadora de Financiamento')
st.header('Saiba quanto vai custar seu financiamento com apenas alguns cliques')
st.text('Os valores aqui apresentados não incluem nenhum tipo de taxa cobrada pelos bancos. Desta forma o valor final será ligeiramente diferente.')

with st.sidebar:

    st.header('Insira as informações abaixo:')

    valor_imovel = st.number_input("🏠 Informe o valor do imóvel (R$): ",
                    value=100_000.0,
                    step=1_000.0,
                    format='%.1f')

    valor_entrada = st.number_input("💰 Qual será o valor da entrada (R$): ",
                    value=50_000.0,
                    step=1_000.0,
                    format='%.1f')

    valor_financiado = st.subheader(f"🏦 O valor financiado será: R$ {valor_imovel - valor_entrada} ")

    prazo = st.number_input("🗓️ Informe o prazo de pagamento (meses): ",
                    value=120,
                    step=1)
    juros_anuais = st.slider("％📱 Qual a taxa negociada % a.a.: ",
                    min_value=1.0,
                    max_value=20.0,
                    step=0.1,
                    format='%.1f')

df = calcula_financiamento(valor_imovel, valor_entrada, prazo, juros_anuais)
df = df[['periodo', 'amortizacao', 'juros_divida','valor_pago_mes','amortizacao_acumulada','juros_acumulados']]
df.sort_values('periodo')

#criar df para os gráficos (sem formatação em string para os valores com R$)
df_gaficos = df[['periodo', 'amortizacao', 'juros_divida','valor_pago_mes','amortizacao_acumulada','juros_acumulados']].copy()

total_pago = df['valor_pago_mes'].sum()
total_pago_formatado = f"R$ {total_pago:,.1f}"
primeira_parcela = df['valor_pago_mes'].iloc[0]
primeira_parcela_formatado = f"R$ {primeira_parcela:,.1f}"
ultima_parcela = df['valor_pago_mes'].iloc[-1]
ultima_parcela_parcela_formatado = f"R$ {ultima_parcela:,.1f}"

# Formatar apenas as colunas monetárias
df[['amortizacao', 'juros_divida','valor_pago_mes','amortizacao_acumulada','juros_acumulados']] = df[['amortizacao', 'juros_divida','valor_pago_mes','amortizacao_acumulada','juros_acumulados']].map('R$ {:,.1f}'.format)

#criar df para os gráficos (sem formatação em string para os valores com R$)

col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.metric(
            label="Valor total pago:",
            value=total_pago_formatado    
        )

with col2:
    with st.container():
        st.metric(
            label="Valor da primeira parcela:",
            value=primeira_parcela_formatado    
        )  

with col3:
    with st.container():
        st.metric(
            label="Valor da última parcela:",
            value=ultima_parcela_parcela_formatado    
        )  




st.dataframe(df[['periodo','amortizacao','juros_divida','valor_pago_mes']],
                hide_index=True)



st.download_button(
    label="Fazer o download da tabela",
    data=conversor(df),
    file_name="valores_financiamento.xlsx"    
    
)

st.subheader('Análise gráfica: Amortização x Juros')                
st.bar_chart(df_gaficos[['amortizacao_acumulada','juros_acumulados']],
             stack=False,
             color=["#FF0000", "#0000FF"]


    )                    

# valor_imovel = float(input('Insira o valor do imóvel: '))
# valor_entrada = float(input('Insira o valor da Entrada: '))
# prazo = int(input('Insira o prazo de pagamento (meses): '))
# juros_anuais = float(input('Inserir a taxa de juros anual (apenas valor): '))




