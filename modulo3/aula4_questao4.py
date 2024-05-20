# Solicitação e entrada dos dados
dist = float (input ("Digite a distância do frete, em km: "))
peso = float (input ("Digite o peso do produto, em kg: "))

# Cálculo do frete
if peso > 10:
    aux = 10
else:
    aux = 0
if dist < 101:
    print (f"Frete = R$ {aux + peso:,.2f}")
else:
    if (dist > 100 and dist < 301):
        print (f"Frete = R$ {aux + peso * 1.5:,.2f}")
    else:
        print (f"Frete = R$ {aux + peso * 2:,.2f}")