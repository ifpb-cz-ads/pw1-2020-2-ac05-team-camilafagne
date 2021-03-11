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
  
lista3 = lista1 + lista2

print(lista3)