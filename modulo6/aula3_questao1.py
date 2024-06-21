lista = []

for i in range (5):
    print ("Digite o ", (i+1), "º valor: ")
    lista.append (input ())

print (lista)
print (lista[0:3])
print (lista[-2:])
print (lista[::-1])
print (lista[0:5:2])
print (lista[1:5:2])