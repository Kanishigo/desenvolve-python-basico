import os, random

tamanho, tam, erro, pos, vitoria = 0, 0, 0, 0, 0

with open ('gabarito_forca.txt', 'r') as l:
    gabarito = l.readlines() #leitura do aruqivo
    palavra = random.choice(gabarito) #sorteia uma palavra
    tamanho = len(palavra) - palavra.count("\n") #calcula o tamanho da palavra

'''    
print (palavra)
print (tamanho)
'''

aux = []
forca = ["", "", "", "", "", "", ""]
i, j, cont = 0, 0, 0

f = open ('gabarito_enforcado.txt')
for lista in f:
    if cont < 11:
        aux.append(lista)
        forca[i] = "".join(aux)
    else:
        i += 1
        cont = 0
        aux.clear()
    cont += 1

print (forca[0])

inicio = list (palavra)
tentativa = list ()
imp_tenta = list ()
aux_cont = 0

for tam in range (tamanho):
    inicio[tam] = "___  "

imp = " ".join(inicio)
print (imp)

while erro < 6:
    letra = input ('\n\nDigite uma letra: ')
    for pos in range (tamanho):
        if letra == palavra[pos]:
            inicio[pos] = letra
            imp = " ".join(inicio)
            aux_cont += 1
            vitoria += 1
    if aux_cont > 0:
        print (forca[erro])
        print (imp)
    else:
        tentativa.insert(erro, letra)
        imp_tenta = " ".join(tentativa)
        erro += 1
        print (forca[erro])
    print ('\n\nPalavra nao possui a letra: ', imp_tenta)
    aux_cont = 0
    if erro == 6:
        print ('\nGAME OVER\n')
    if vitoria == tamanho:
        print ('\nPARABENS! VOCE ACERTOU!\n')
        break

f.close()