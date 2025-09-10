
n = 5
i = 0
valores = []
positivos = 0
negativos = 0
par = 0
impar = 0


while i<n:
  x = int(input())
  valores.append(x)
  if x >0:
    positivos = positivos+1
  elif x < 0:
    negativos = negativos+1
  if x%2 == 0:
    par = par + 1
  else:
    impar = impar+1
  i = i+1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")