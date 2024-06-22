celular = input ("Digite o número de seu celular: ")
inicio = True

if len(celular) == 9:
    if celular[0] == "9":
        inicio = True
    else:
        inicio = False
        print ("ATENÇÃO: Número não inicia com 9!")
else:
    celular = "9"+celular

inicio = celular[:5]
ult = celular[5::]

print ("Número: ", inicio+"-"+ult)

