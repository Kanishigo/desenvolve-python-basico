import random

lista1, lista2, intersecao = [], [], []
for i in range(20):
    lista1.append(random.randint(0,50))
    lista2.append(random.randint(0,50))

for aux in lista1:
    if aux in lista2 and aux not in intersecao:
        intersecao.append(aux)

intersecao.sort()
print (sorted(lista1))
print (sorted(lista2))
print (intersecao)

for i in intersecao:
    print (f"{i}: Lista 1 - {lista1.count(i)} vezes, Lista 2 - {lista2.count(i)} vezes.")
