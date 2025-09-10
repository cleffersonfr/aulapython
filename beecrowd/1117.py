
notas = []
while len(notas)<2:
    nota = float(input())
    if nota >= 0 and nota <=10:
        notas.append(nota)
    else:
        print("nota invalida")

media = (notas[0]+notas[1])/2

print(f"media = {media:.2f}")