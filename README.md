# aulapython

## Tipo dados primitivos

- Integer -> numero inteiro: ex 3 
- Float-> Numero de ponto flutuante-> 3.14
- Boolean(bool) -> True of False -> 1 ou 0  
- String-> Conjunto de caracteres -> "" ou '' -> exemplo "minha frase", "2"

## Operadores aritimeticos

- Soma => +
- Subtracao => -
- Divisao => /
- Multiplicacao => *
- Resto => %
- Divisao inteira => //
- Exponenciacao => **

## Input -> entrada de strings via terminal

## Output(print) : exibir dados no terminal

```python

print("Calculo de IMC")
print("Digite a sua altura: ")
altura = float(input())
print("Digite o seu peso:")
peso = float(input())

imc = peso/(altura**2)

print("Seu imc vale:",imc)
```

## Condicionais

### Operadores

- igualdade ==
- diferenca !=
- maior >
- maior igual >=
- menor <
- menor igual <=
- negacao not

### if - controle fluxo

```python

x = 4

if x>6:
    print(1)

elif x>2:
    print(2)

if x>3:
    print(3)
else:
    print(4)

```


```python


a,b,c,d = list(map(float,input().split()))

media = (a * 2 + b * 3 + c * 4 + d) / 10 
print(f"Media: {media:.1f}")


if media >= 7:
    print("Aluno aprovado.")
elif media>=5:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    if ((nota_exame + media) / 2) > 5:
        print("Aluno aprovado.")
        nova_media = (nota_exame + media)/2
        print(f"Media final: {nova_media:.1f}")
    else:
        print("Aluno reprovado.")
else:
    print("Aluno reprovado.")



hora_inicial,hora_final = list(map(int,input().split()))
if hora_final == hora_inicial:
  print("O JOGO DUROU 24 HORA(S)")
elif hora_final > hora_inicial:
  duracao = int(hora_final - hora_inicial)
  print(f"O JOGO DUROU {duracao} HORA(S)")
else:
  duracao = 24 - (hora_inicial - hora_final)
  print(f"O JOGO DUROU {duracao} HORA(S)")
    

tipo1 = input()
tipo2 = input()
tipo3 = input()
animal = 0

if tipo1 == "vertebrado":
  if tipo2 == "ave":
    if tipo3 == "onivoro":
      animal = "pomba"
    else:
      animal = "aguia"
  elif tipo2 =="mamifero":
    if tipo3 == "onivoro":
      animal = "homem"
    else:
      animal = "vaca"
else:
  if tipo2 == "inseto":
    if tipo3 == "hematofago":
      animal = "pulga"
    else:
      animal ="lagarta"
  elif tipo2 =="anelideo":
    if tipo3 == "hematofago":
      animal = "sanguessuga"
    else:
      animal = "minhoca"
print(animal)

```

### Problemas

#### Repeticao

- 1064,1066, 1078

#### Listas

- 1175, 1176

### Jogo da forca

- falar basico sobre funcao