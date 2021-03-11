expressao = str(input("Informe uma expressão:"))
pilha = 0
for cont in expressao:
    if cont == "(":
        pilha += 1
    if cont == ")":
        pilha -= 1
    if pilha < 0:
        break
if pilha == 0:
    print("A expressão informada é valida ^-^")
else:
    print("A expressão informada não é valida ;-;")

