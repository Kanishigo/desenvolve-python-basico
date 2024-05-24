# Entrada de dados e inicialização das variáveis
n = int (input ("Digite um número inteiro: "))
maior = 0

# Validação das condições
while n>0:
    x = int (input ("Digite outro número inteiro: "))
    if x > maior:
        maior = x
    n -= 1
print (maior)