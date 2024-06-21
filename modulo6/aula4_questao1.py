lista, lista3, lista4 = [], [], []

for i in range(20,51):
    lista.append(i)

pares = [par for par in lista if par % 2 == 0]

#print (lista)
print ("Pares:\n", pares)
print ("\nParte 2")

lista2 = [1,2,3,4,5,6,7,8,9]
quadrado = [n**2 for n in lista2]

print ("Quadrados:\n", quadrado)
print ("\nParte 3:")

for n in range (1, 101):
    lista3.append (n)

divisao = [div for div in lista3 if div % 7 == 0]
print ("Divisíveis por 7:\n", divisao)
print ("\nParte 4:")

for j in range(0, 30, 3):
    lista4.append(j)

elemento = ["Par" if aux % 2 == 0 else "Impar" for aux in lista4]
print (lista4)
print (elemento)