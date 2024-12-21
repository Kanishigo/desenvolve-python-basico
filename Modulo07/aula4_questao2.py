import os

with open ('frase.txt', 'r') as f:
    aux = f.read()
    with open ('palavras.txt', 'w') as p:
        p.write (aux)

with open ('palavras.txt', 'r') as p:
    aux2 = p.read()

linhas = aux2.split()
itens = list (linhas)
itens = [i+'\n' for i in itens]

with open('palavras.txt', 'w') as p:
    p.writelines(itens)

z = open ('palavras.txt', 'r')
print (z.read())
z.close()
