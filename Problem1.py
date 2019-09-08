
qa = int(input("Quantidade de elementos: "))
k = int(input("valor da soma: "))
lista = []

for r in range(qa):
  a = int(input("elemento:"))
  lista.append(a)

i = len(lista) - 1
for e in lista:
  if(lista[i] + e == k):
    print("sim")
    break
  else:
    print("nao")
    break
  i-=1

  
