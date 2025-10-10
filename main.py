<<<<<<< Updated upstream
# ## Loop

# # i = 0
# # while True:
# #   i = i+1
# #   if i ==1000:
# #     break
# #   print(i)

# # print("saiu")
  

# # i = 0
# # while i<1000:
# #   i = i+1
# #   print(i)

# # print("saiu")
# #index 0   1.2. 3
# l =   ["a",2,5,[4,6]]

# print(l[3][1])
# n = int(input())
# cliques = list(map(int,input().split()))
# i=0
# a = -1
# b = -1
# # while i < len(cliques):
# #   i = i+1
# #   x = cliques[i]
# #   a =a*(-1)

# #   if x ==2:
# #     b= b*(-1)
# qtd =0
# # while i< len(cliques):
# #   if cliques[i]==2:
# #     qtd= qtd + 1
# qtd =cliques.count(2)
# if len(cliques)%2==0:
#   print(0)
# else:
#   print(1)

# if qtd%2==0:
#   print(0)
# else:
#   print(1)

# n = int(input())
# i = 0
# qtd = 0
# while i < n:
#   i = i + 1
#   latas, copos = list(map(int,input().split()))
#   if latas > copos:
#     qtd = qtd + copos

# print(qtd)

  

# n = int(input())
# dias = 1
# i=0
# acumulado = 0
# while i<n:
#   acesso = int(input())

#   acumulado = acumulado + acesso
#   if acumulado < 1000000:
#     dias = dias + 1
  
  
#   i = i+1

# print(dias)

# l =[1,2,3,4]
# print(l[2])
# len(l)
# l.append(x)

# n = int(input())
# i = 0
# q = 0
# valor = list(map(int,input().split()))
# while i < n-2:
#   i = i + 1
#   if valor [i] == 1 and valor[i+1]==0 and valor[i+2]==0:
#     q = q+1
# print(q)

# quantidade_numeros_lista = int(input())
# indice_lista = 0
# vezes_que_aparece_100 = 0
# numeros = list(map(int,input().split()))
# while indice_lista < quantidade_numeros_lista-2:
#   if numeros[indice_lista] == 1 and numeros[indice_lista + 1] == 0 and numeros[indice_lista + 2] == 0:
#     vezes_que_aparece_100 = vezes_que_aparece_100 + 1
#     indice_lista = indice_lista + 1
# print(vezes_que_aparece_100)

# n_celulas = int(input())
# valores_celulas= [0]
# i=0

# while i<n_celulas:
#   x = int(input())
#   valores_celulas.append(x)
#   i +=1

# valores_celulas.append(0)
# i = 1

# while i < n_celulas-1:
#   campo_minado = 0
#   #verificar celula atual
#   if valores_celulas[i] > 0:
#     campo_minado = campo_minado + 1
#     #verifica celula anterior
#   if valores_celulas[i - 1] > 0:
#     campo_minado = campo_minado + 1
#   #verifica celula posterior
#   if valores_celulas[i + 1] > 0:
#     campo_minado = campo_minado + 1
  
#   i = i + 1
#   print(campo_minado)

# def valor(preco, qtd):

#   if qtd<0:
#     return 0

#   return preco*qtd
  
# def valor_total(precos_list,qtd_list):
#   soma = 0
#   for i in range(len(precos_list)):
#     soma += valor(precos_list[i],qtd_list[i])
#   return
# r=valor_total(2,-3)
# print(r)
=======
# class Pessoa():
#     def __init__(self,nome,idade):
#         self.nome = nome
#         self.idade = idade
    
#     def diz_ola(self, nome):
#         print(f"Ola {nome} eu sou {self.nome}")

# Dicionario -> chave: valor
# nao ordenado
# Json

# d = {
#     "nome":"marcus",
#     "materias": [],
#     "idade": 23

# }
# #((nome,marcus),(materias,[]))

# print(d['altura'])# quebra o codigo
# print(d.get('altura'))#-> none
# d["altura"] = 1.74
# print(d['nome'])

# print(d.keys())
# print(d.values())

# for chave,valor in d.items():
#     if chave == 'nome':
#         print(valor)


# palavra  = 'paralelepipedo'
# d={}
# for letra in palavra:
#     if d.get(letra) ==None:
#         d[letra] =0
    
#     d[letra] +=1

# recorde = -1
# letra =None
# for chave, valor in d.items():
#     if valor> recorde:
#         recorde = valor
#         letra = chave
    

# print(letra,recorde)

def print_info_medico(medico_dict):
    print("="*20)
    print(f"Dados do medico: {medico_dict['nome']}")
    print(f"Especialidade: {medico_dict['especialidade']}")
    print(f"Hospitais:")
    for hospital in medico_dict['hospitais']:
        print(f"    Hospital: {hospital}")

# d = {especialidade:[medicos]}        

def get_medicos_por_especialidade(medicos_dict):
    d = {}
    for medico in medicos:
        nome = medico['nome']
        especialidade = medico['especialidade']
        if d.get(especialidade) ==None:
            d[especialidade] = []
        d[especialidade].append(nome)
    return d

#gerar um dicionario {hospital->[nomes]}
#gerar um dicionario {hospital -> [{nome,especilidade}]}
medicos = [
    {
        "nome": "Dr. João Silva",
        "especialidade": "Cardiologia",
        "hospitais": ["Hospital Central", "Clínica Coração Saudável"]
    },
    {
        "nome": "Dra. Maria Oliveira",
        "especialidade": "Ortopedia",
        "hospitais": ["Hospital Ortopédico", "Hospital das Clínicas"]
    },
    {
        "nome": "Dr. Pedro Santos",
        "especialidade": "Neurologia",
        "hospitais": ["Hospital Neurológico", "Hospital Central"]
    },
    {
        "nome": "Dra. Ana Costa",
        "especialidade": "Pediatria",
        "hospitais": ["Hospital Infantil", "Clínica São Lucas"]
    },
    {
        "nome": "Dr. Ricardo Lima",
        "especialidade": "Dermatologia",
        "hospitais": ["Clínica da Pele", "Hospital Universitário"]
    },
    {
        "nome": "Dra. Fernanda Rocha",
        "especialidade": "Cardiologia",
        "hospitais": ["Hospital Central", "Hospital Universitário"]
    },
    {
        "nome": "Dr. Marcos Pereira",
        "especialidade": "Ortopedia",
        "hospitais": ["Hospital Ortopédico", "Hospital Central"]
    },
    {
        "nome": "Dra. Carolina Mendes",
        "especialidade": "Pediatria",
        "hospitais": ["Hospital Infantil", "Hospital das Clínicas"]
    },
    {
        "nome": "Dr. Rafael Souza",
        "especialidade": "Neurologia",
        "hospitais": ["Hospital Neurológico", "Clínica São Lucas"]
    },
    {
        "nome": "Dra. Beatriz Almeida",
        "especialidade": "Dermatologia",
        "hospitais": ["Clínica da Pele", "Hospital das Clínicas"]
    }
]




# for medico in medicos:
#     print_info_medico(medico)

print(get_medicos_por_especialidade(medicos))
>>>>>>> Stashed changes

