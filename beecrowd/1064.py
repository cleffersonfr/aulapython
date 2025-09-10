
valores = []
qtd_valores = 6
i = 0
valores_positivos = 0
media = 0
soma = 0

while i<qtd_valores:
  x = float(input())
  valores.append(x)
  if x > 0:
    valores_positivos = valores_positivos+1
  i = i +1

for n in valores:
  if n > 0:
    soma = soma + n
    n = n + 1
media = soma / valores_positivos

print(f"{valores_positivos} valores positivos")
print(f"{media:.1f}")