lista1, lista2, result, final = [], [], [], []

tam1 = int(input("Digite a quantidade de elementos da lista 1: "))
print ("Digite os ", tam1, " elementos da Lista 1: ")

for i in range(tam1):
    lista1.append(input())

tam2 = int(input("Digite a quantidade de elementos da lista 2: "))
print ("Digite os ", tam2, " elementos da Lista 2: ")

for i in range(tam2):
    lista2.append(input())

result = lista1+lista2

for aux in range(len(result)):
    if aux % 2 == 0:
        final.append(result[aux])
    else:
        final.append(result[aux])

print (lista1)
print (lista2)
print (result)
print (final)