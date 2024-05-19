# Entrada do comprimento do terreno
comp = int (input ("Digite o comprimento do terreno: "))

# Entrada da largura do terreno
larg = int (input ("Digite a largura do terreno: "))

# Entrada do valor do metro quadrado da região
preco = float (input ("Digite o valor do m² na região: "))

# Cálculo da área do terreno
area = comp * larg

# Cálculo do valor do terreno
valor = area * preco

# Impressão dos resultados da área e do valor do terreno
print (f"O terreno possui {area}m² e custa R$ {valor:,.2f}")