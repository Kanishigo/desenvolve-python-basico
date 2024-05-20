# Entrada dos dados
av = int (input ("Digite sua avaliação (1 a 5): "))

# Validação dos dados e impressão do resultado
if av == 1:
    print ("Ruim")
else:
    if av == 2:
        print ("Regular")
    else:
        if av == 3:
            print ("Bom")
        else:
            if av == 4:
                print ("Muito Bom")
            else:
                print ("Excelente")