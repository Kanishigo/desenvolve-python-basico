import random

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave_aleatoria = random.randint(1,10)
cript, cript_aux, lista_cript = [], [], []
print ("Chave cript: ", chave_aleatoria)

for i in range(len(nomes)):
    aux = list(nomes[i])
    #print ("aux1: ", aux)
    for letra in aux:
        cript_aux.append (ord (letra)+chave_aleatoria)
        #print ("Letra: ", letra)
        #print ("cript aux: ", cript_aux)
    for conversao in cript_aux:
        lista_cript.append (chr (conversao))  
        #print ("Convertendo: ", conversao)
        #print ("lista_cript: ", lista_cript)
    cript.append("".join(lista_cript))
    cript_aux, lista_cript = [], []

print ("Nomes cript: ", cript)
    