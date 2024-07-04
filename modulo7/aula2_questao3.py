while True:

    palavra = input ("Digite uma palavra (para sair digite 'fim'): ")

    original = palavra
    palavra = palavra.lower()
    palavra = palavra.split()
    palavra = "".join(list(palavra))
    palavra = palavra.strip("!@#$%¨&*?")

    if palavra != "fim":        
        invertida = palavra[::-1]
        invertida = invertida.strip()
        if palavra == invertida:
            print (original, "é um políndromo.")
        else:
            print (original, "não é um políndromo.")
    else:
        break

print ("Fim do programa.")