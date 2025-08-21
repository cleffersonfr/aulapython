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

quantidade_numeros_lista = int(input())
indice_lista = 0
vezes_que_aparece_100 = 0
numeros = list(map(int,input().split()))
while indice_lista < quantidade_numeros_lista-2:
  if numeros[indice_lista] == 1 and numeros[indice_lista + 1] == 0 and numeros[indice_lista + 2] == 0:
    vezes_que_aparece_100 = vezes_que_aparece_100 + 1
    indice_lista = indice_lista + 1
  print(vezes_que_aparece_100)