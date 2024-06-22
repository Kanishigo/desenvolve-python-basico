def calc_dig (resultado):
    if resultado % 11 < 2:
        return 0
    else:
        return (11 - (soma % 11))

cpf = input ("Digite seu CPF: ")

cpf_num, verificador = [], []
soma = 0
fator_mult = 10

cpf_string = list(cpf)
ult = "".join(cpf_string[9::])
del cpf_string[:-3:-1]

for i in range(len(cpf_string)):
    cpf_num.append (int(cpf_string[i]))
    soma += cpf_num[i]*fator_mult
    fator_mult -= 1

dig1 = calc_dig(soma)

cpf_num.append(dig1)
soma = 0
fator_mult = 11

for i in range(len(cpf_num)):
    soma += cpf_num[i]*fator_mult
    fator_mult -= 1

dig2 = calc_dig(soma)

verificador.append(str(dig1))
verificador.append(str(dig2))
validador = "".join(verificador)

print (cpf)
print ("Dígito validador informado: ", ult)
print ("Validador calculado: ", validador)

if ult == validador:
    print ("CPF Válido!")
else:
    print ("CPF Inválido!")
