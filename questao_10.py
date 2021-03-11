estoque={ "tomate": [ 1000, 2.30], "alface": [ 500, 0.45], "batata": [ 2001, 1.20], "feijao": [ 100, 1.50] }

total = 0
print("Vendas:\n")

while True:
  produto = input("\nInforme o produto, se desejar encerrar digite 0: ")

  if produto in estoque:
    quantidade = int(input("Informe a quantidade: "))

    if quantidade <= estoque[produto][0]:
      preço = estoque[produto][1]
      custo = preço * quantidade
      print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade,preço,custo))	 
      estoque[produto][0] -= quantidade
      total+=custo

    else:
      print("Quantidade indisponível!")

  elif produto == '0':
    break
  
  else:
    print("Produto não encontrado no estoque!")
  
    
print("\nCusto total: %21.2f\n" % total)
print("Estoque:\n")

for chave, dados in estoque.items():
	print("Descrição: ", chave)
	print("Quantidade: ", dados[0])
	print("Preço: %6.2f\n" % dados[1])
