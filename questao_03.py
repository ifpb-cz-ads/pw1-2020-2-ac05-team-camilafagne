lista1 = []
lista2 = []

print("Vamos preencher a primeira lista!")

while True:
  num = int(input("Informe um valor, se desejar digite 0: "))

  if num == 0:
    break

  lista1.append(num)

print("\nAgora vamos preencher a segunda lista! ^-^")
while True:
  num = int(input("Informe um valor, se desejar encerrar digite 0: "))

  if num == 0:
    break

  lista2.append(num)

listaAux = []
aux1=0
verifica=0

listaAux = lista1

aux1 = 0 
verifica = 0

for i in range(len(lista2)):
  aux1 = lista2[i]
  verifica = 0
  for p in range(len(listaAux)):
    if aux1 == listaAux[p]:
      verifica = 1
  if verifica == 0:
    listaAux.append(lista2[i])
    
aux2 = 0
verifica = 0

lista3 = []

for k in range(len(listaAux)):
  aux2 = listaAux[k]
  verifica = 0
  for j in range(k+1,len(listaAux)):
    if aux2 == listaAux[j]:
      verifica = 1
  if verifica == 0:
     lista3.append(listaAux[k])

print(lista3)