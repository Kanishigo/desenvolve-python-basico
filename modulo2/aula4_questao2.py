# Entrada do valor, em inteiro, da temperatura em Fahrenheit
temp_f = int (input ("Digite o valor da temperatura em Fahrenheit: "))

# Conversão da temperatura de Fahrenheit para Celsius
conversao = int((temp_f - 32) * (5/9))

# Impressão da conversão
print (f"{temp_f} graus Fahrenheit são {conversao} graus Celsius.")