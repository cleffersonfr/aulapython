n = 20
i = 0
lista = []
posicao = n-1
ordem = 0 

while i<n:
  v = int(input())
  lista.append(v)
  i = i+1



while posicao >= 0:
  print(f"N[{ordem}] = {lista[posicao]}")
  posicao = posicao - 1
  ordem = ordem +1