# Entrada de dados e inicialização das variáveis
n1 = float (input ("Digite a nota 1: "))
n2 = float (input ("Digite a nota 2: "))
n3 = float (input ("Digite a nota 3: "))
m = (n1 + n2 + n3) / 3

# Validação das condições
if m >= 60:
    print ("Aprovado")
elif m >= 40:
    print ("Recuperação")
else:
    print ("Reprovado")
print ("Fim")