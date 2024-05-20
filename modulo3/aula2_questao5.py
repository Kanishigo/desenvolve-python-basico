# Solicitação e entrada de dados
sexo = input ("Digite seu gênero (M/F): ")
idade = int (input ("Digite sua idade: "))
exp = int (input ("Digite seu tempo de serviço, em anos: "))

# Validação das condicionantes
v_idade = (sexo == "M" and idade > 64) or (sexo == "F" and idade > 59)

# Impressão dos resultados
print (f"Apto para aposentar: {v_idade or exp > 29 or (idade > 59 and exp > 24)}")