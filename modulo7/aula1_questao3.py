frase = input ("Digite uma frase: ")
cont = 0

for espaco in frase:
    if espaco == " ":
        cont += 1

print ("Espaços em branco: ", cont)