import pandas as pd

def input_tabela_mestre(caminho = 'tabela_mestre_apresentacao.xlsx'):

    forecast = pd\
        .read_excel(caminho,sheet_name='forecast',skiprows=2)\
        .dropna(axis=1)
    
    forecast.rename(columns={'versão':'versao','mês':'mes','At Budget Rate': 'USD'},inplace=True)

   
    actual = pd\
        .read_excel(caminho, sheet_name='actual',skiprows=2)\
        .dropna(axis=1)
    
    actual.rename(columns={'Unnamed: 0':'site','Unnamed: 1':'conta','Unnamed: 2':'ano','Unnamed: 3': 'cenario',
                            'Unnamed: 4':'versao','Unnamed: 5':'mes','At Budget Rate': 'USD'},inplace=True)
        
    df_index = pd.read_excel(caminho, sheet_name='index')

    return actual,forecast,df_index
