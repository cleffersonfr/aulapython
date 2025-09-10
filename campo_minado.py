#n_celulas = int(input())
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

# n_celulas = int(input())
# i = 0
# valores = [0]
# cm = []
 

# while i < n_celulas:
#   x = int(input())
#   valores.append(x)
#   i = i + 1
# valores.append(0)
# i = 1

# while i < n_celulas+1:
#   resultado = 0

#   if valores[i]>0:
#     resultado = resultado+1
#   if valores[i+1]>0:
#     resultado = resultado+1
#   if valores[i-1]>0:
#     resultado = resultado+1
     
#   cm.append(resultado)
#   i = i+1

#   #print(valores)
#   #print(resultado)
# print(cm)

def is_vitoria(palavra_atual):
    if not "*" in palavra_atual:
        return True
    return False