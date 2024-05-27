# Importação das bibliotecas
import math, random

# Entrada e inicialização das variáveis
soma = 0
n = int (input ("Digite a quantidade de números aleatórios desejados: "))

# Somatório dos n números aleatórios
for i in range (n):
    soma += random.randint(1,100)

# Impressão da raíz quadrada
print (f"A raiz quadrado da somatória dos {n} números aleatórios é: {math.sqrt(soma):.2f}")