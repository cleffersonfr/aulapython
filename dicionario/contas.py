TIPOS = [
    {"id": 1, "valor": "Alimentação"},
    {"id": 2, "valor": "Transporte"},
    {"id": 3, "valor": "Lazer"},
    {"id": 4, "valor": "Saúde"},
    {"id": 5, "valor": "Educação"},
]

gastos = [
    {"descricao": "Supermercado", "tipo": 1, "valor": 250.75},
    {"descricao": "Uber", "tipo": 2, "valor": 35.00},
    {"descricao": "Cinema", "tipo": 3, "valor": 45.00},
    {"descricao": "Consulta médica", "tipo": 4, "valor": 180.00},
    {"descricao": "Mensalidade faculdade", "tipo": 5, "valor": 1200.00},
    {"descricao": "Restaurante", "tipo": 1, "valor": 90.50},
    {"descricao": "Ônibus", "tipo": 2, "valor": 5.50},
]

def get_valor_total(gastos_list):
    gasto_total = 0
    for gasto in gastos:
        gasto_total = gasto_total + gasto['valor']

    return gasto_total

def get_nome_do_tipo(gasto):
    id_gasto = gasto['tipo']
    for tipo in TIPOS:
        if tipo['id'] == id_gasto:
            return tipo['valor']    
    
    return None


def converte_tipo_gasto(gasto_list):
    for gasto in gasto_list:
        gasto['tipo'] = get_nome_do_tipo(gasto)
    
    return gasto_list
    
def agrupa_gastos_por_tipo(gasto_list):
    resposta = {}
    gasto_list = converte_tipo_gasto(gasto_list)
    for gasto in gasto_list:
        tipo = gasto['tipo']

        if tipo == None:
            tipo = 'invalidos'

        if resposta.get(tipo)==None:
            resposta[tipo] = 0

        resposta[tipo]+= gasto['valor']
    
    return resposta


print(agrupa_gastos_por_tipo(gastos))