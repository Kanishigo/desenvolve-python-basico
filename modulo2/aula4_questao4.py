# Entrada do valor, em inteiro, da quantia
valor = int (input ("Digite o valor a receber, sem considerar os centavos: "))

# Calculando a quantidade de notas por valor
n_100 = valor//100
# Guardando o resto da divisão para os próximos valores de notas
resto = valor%100

n_50 = resto//50
resto %= 50

n_20 = resto//20
resto %= 20

n_10 = resto//10
resto %= 10

n_5 = resto//5
resto %= 5

n_2 = resto//2
resto %= 2

n_1 = resto//1
resto %= 1

print (f"{n_100} nota(s) de R$100,00")
print (f"{n_50} nota(s) de R$50,00")
print (f"{n_20} nota(s) de R$20,00")
print (f"{n_10} nota(s) de R$10,00")
print (f"{n_5} nota(s) de R$5,00")
print (f"{n_2} nota(s) de R$2,00")
print (f"{n_1} nota(s) de R$1,00")
