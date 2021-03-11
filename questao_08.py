T = [ -10, -8, 0, 1, 2, 5, -2, -4]

menor= T[0]
maior = T[0]
media = T[0]
soma = 0

for i in range(len(T)):
  if T[i] < menor:
    menor = T[i]
  if T[i] > maior:
    maior = T[i]
  soma = soma + T[i]

media = soma / len(T)

print("A maior temperatura é %d, a menor temperatura é %d e a temperatura mediana é %d" % (maior, menor, media))
