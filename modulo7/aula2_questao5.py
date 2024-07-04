import random

def embaralhar (frase):
    
    frase = list (frase)
    tamanho = len (frase)
    primeira = frase[0]
    ultima = frase[tamanho-1]
    random.shuffle (frase)
    frase[0] = primeira
    frase[tamanho-1] = ultima
    final = "".join(frase)

    return (final)

frase = input ("Digite uma frase: ")

print (embaralhar(frase))