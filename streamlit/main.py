import streamlit as st

st.title("💱 Conversor de Moedas (Simulação)")

# Dicionário de cotações fixas (exemplo)
cotacoes = {
    "USD": 5.20,   # 1 USD = 5.20 BRL
    "EUR": 5.60,   # 1 EUR = 5.60 BRL
    "BRL": 1.00,   # Real é a base
    "BTC": 250000.00  # 1 BTC = 250 mil BRL
}

moedas = list(cotacoes.keys())

moeda1 = st.selectbox("Selecione a moeda de origem", moedas)
moeda2 = st.selectbox("Selecione a moeda de destino", moedas)

valor = st.number_input("Digite o valor a ser convertido", min_value=0.00, format="%.2f")

if st.button("Converter"):
    # Conversão simples via BRL como base
    valor_em_brl = valor * cotacoes[moeda1]
    resultado = valor_em_brl / cotacoes[moeda2]
    st.success(f"O valor de {valor:.2f} {moeda1} em {moeda2} é {resultado:.2f}")
