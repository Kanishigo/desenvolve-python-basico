frase = input ("Digite uma frase: ")

cont = 0
idx = []

for i in range(len(frase)):
    if frase[i] in "aeiouAEIOU":
        cont += 1
        idx.append (i)

print ("Quantidade de vogais na frase: ", cont)
print ("Indices das vogais:\n", idx)
