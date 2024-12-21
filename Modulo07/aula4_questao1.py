import os, sys

with open ('frase.txt', 'r+') as f:
    f.write (input ("Digite uma frase: "))

f = open('frase.txt', 'r')
print ("Frase digitada: ", f.read())
print ("Arquivo salvo em: ", os.path.abspath('frase.txt'))
