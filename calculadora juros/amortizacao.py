
import pandas as pd
import streamlit as st


print('================================================================')
print('Periodo // Amortização // Juros // Pagamento Mês')
def calcula_financiamento(valor_imovel, valor_entrada, prazo, juros_anuais):
    valor_financiamento = valor_imovel - valor_entrada
    juros_mensais = (1+(juros_anuais/100))**(1/12)-1
    parcela = 0
    amortizacao_divida = valor_financiamento / prazo
    pgto_acumulado = 0
    juros_acumulados = 0
    amortizacao_acumulada = valor_financiamento
    parcelas = []
    for periodo in range(1,prazo+1):
        parcela_acumulada = parcela
        juros_divida = (valor_financiamento - parcela_acumulada) * juros_mensais
        valorpagomes = amortizacao_divida + juros_divida
        pgto_acumulado = pgto_acumulado + valorpagomes
        parcela = parcela + amortizacao_divida
        juros_acumulados = juros_acumulados + juros_divida
        amortizacao_acumulada = amortizacao_acumulada - amortizacao_divida
        parcela_dict = {
            'parcela_acumulada':parcela,
            'valor_pago_mes':valorpagomes,
            'juros_divida': juros_divida,
            'amortizacao': amortizacao_divida,
            'periodo': periodo,
            'pagto_acum': pgto_acumulado,
            'juros_acumulados': juros_acumulados,
            'amortizacao_acumulada': amortizacao_acumulada
            
        }
        parcelas.append(parcela_dict)

    df = pd.DataFrame(parcelas)
    df = df[['periodo','amortizacao','juros_divida','valor_pago_mes','pagto_acum','juros_acumulados','amortizacao_acumulada']]
    #print(df.head())
    df.to_excel('teste_financiamento.xlsx')
    return df

    #print(f'{periodo} - {amortizacao_divida:.1f} - {juros_divida:.1f} - {valorpagomes:.1f} - {pgto_acumulado:.1f}')