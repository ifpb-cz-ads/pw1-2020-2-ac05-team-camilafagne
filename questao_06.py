L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
v=int(input("Digite outro valor a procurar:"))

x=0
while x<len(L):
  if L[x]==p:
    		print("%d achado" % (p))
    		break
  x+=1

y=0
while y<len(L):
  if L[y]==v:
    		print("%d achado" % (v))
    		break
  y+=1

if len(L) != p and x == len(L):
	print("%d não encontrado" % p)
  
else:
  if x < y:
    print("%d foi encontrado primeiro" % p)
 

if len(L) != v and y == len(L):
	print("%d não encontrado" % v)
  
else:
  if y < x:
    print("%d foi encontrado primeiro" % v)