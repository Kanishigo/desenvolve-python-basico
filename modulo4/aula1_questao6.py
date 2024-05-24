# Entrada do número de experimentos e inicialização das variáveis
n = int (input ("Digite o número de experimentos: "))
sapo = 0
coelho = 0
rato = 0
soma = 0
cont = 1    # Variável criada somente para melhorar a legibilidade para o usuário

# Solicitação e armazenamento da quantidade de cobaias utilizadas
while n>0:
    quantia = int (input (f"Digite a quantidade de cobaias utilizadas no experimento {cont}: "))
    soma += quantia
    tipo = input ("Digite a letra que representa a cobaia utilizada (S: Sapo, R: Rato, C: Coelho): ")
    if tipo == "S":
        sapo += quantia
    elif tipo == "R":
        rato += quantia
    else:
        coelho += quantia
    cont += 1
    n -= 1

# Cálculo das porcentagens
perc_rato = rato/soma*100
perc_sapo = sapo/soma*100
perc_coelho = coelho/soma*100

# Impressão dos resultados
print (f"Total: {soma} cobaias")
print (f"Total de coelhos: {coelho}")
print (f"Total de ratos: {rato}")
print (f"Total de sapos: {sapo}")
print (f"Percentual de coelhos: {perc_coelho:.2f}%")
print (f"Percentual de ratos: {perc_rato:.2f}%")
print (f"Percentual de sapos: {perc_sapo:.2f}%")