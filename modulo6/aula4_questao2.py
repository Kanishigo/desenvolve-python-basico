vogal, consoante = [], []

frase = input ("Digite uma frase: ")

letras = list(frase)

letras.remove(" ")

for l in letras:
    if l in "aeiouAEIOU":
        vogal.append (l)
    else:
        consoante.append(l)

print (frase)
print ("Vogais: ", sorted(vogal))
print ("Consoantes: ", sorted(consoante))