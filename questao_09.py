string = input("Informe a palavra ou frase: ")

dic = {}

for x in string:
  if x == ' ':
    continue
  else:
    y = string.count(x)
    dic[x] = y

print(dic)