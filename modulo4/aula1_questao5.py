# Entrada da quantidade de respondentes
n = int (input ("Digite a quantidade respondentes: "))
cont = 1    # Variável criada somente para melhorar a legibilidade para o usuário
soma = 0

# Solicitação das idades e cálculo da média das idades
while n>0:
    idade = int (input (f"Digite a idade do entrevistado {cont}: "))
    soma += idade
    n -= 1
    cont += 1
media = soma/(cont-1)
print (f"A idade média dos {cont-1} respondentes é: {media}")