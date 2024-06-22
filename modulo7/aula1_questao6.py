frase = "Meu amor mora em Roma e me deu um ramo de flores"
objetivo = sorted("amor")
anagramas = []

lista_palavras = frase.lower().split()
for palavra in lista_palavras:
    if sorted(palavra) == objetivo:
        anagramas.append(palavra)

print ("Anagramas: ", anagramas)