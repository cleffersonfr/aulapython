lista_carros = []

def calcula_comissao(valor_venda, percentual):
    comissao = valor_venda * percentual
    return comissao

def adiciona_carro(carros_list):
    valor = float(input())
    ano = int(input())
    modelo = input()
    d = {
        "valor":valor,
        "ano": ano,
        "modelo": modelo

    }
    carros_list.append(d)

    return d

def acha_carro(modelo, carros_list):
    for carro in carros_list:
        if carro.get('modelo') == modelo:
            return carro
    return 'not found'

