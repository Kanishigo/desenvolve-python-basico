# Entrada dos dados da compra 1
p = input ("Digite o nome do produto 1: ")
preco = float (input ("Digite o preço unitário do produto 1: "))
qtde = int (input ("Digite a quantidade comprada do produto 1: "))

# Cálculo da compra 1
total = preco * qtde

# Entrada dos dados da compra 2
p = input ("Digite o nome do produto 2: ")
preco = float (input ("Digite o preço unitário do produto 2: "))
qtde = int (input ("Digite a quantidade comprada do produto 2: "))

# Cálculo do total da compra acrescido da compra 2
total += (preco * qtde)

# Entrada dos dados da compra 3
p = input ("Digite o nome do produto 3: ")
preco = float (input ("Digite o preço unitário do produto 3: "))
qtde = int (input ("Digite a quantidade comprada do produto 3: "))

# Cálculo do total acumulado acrescido da compra 3
total += (preco * qtde)

# Impressão do total da compra
print (f"Total: R$ {total:,.2f}")