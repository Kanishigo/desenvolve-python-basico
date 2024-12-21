import os

total, maior, pos, cont, qtde_nonato, qtde_iria = 0, 0, 0, 0, 0, 0

with open ('estomago.txt', 'r') as t:
    linhas = t.readlines()
    total = len (linhas)

t = open ('estomago.txt')
for texto in t:
    cont += 1
    if maior < len (texto):
        maior = len (texto)
        pos = cont
t.close()

t = open ('estomago.txt')
for linha in t:
    if linha.startswith ('Nonato' or 'nonato'):
        qtde_nonato += 1
    if linha.startswith ("Íria" or "íria"):
        qtde_iria += 1
t.close()        

print (linhas[:25],'\nTotal de linhas: ', total)
print ('A linha com maior linha de caractere - Linha nº: ', pos)
print("Qauntidade do nome 'Nonato': ", qtde_nonato)
print("Qauntidade do nome 'Íria': ", qtde_iria)