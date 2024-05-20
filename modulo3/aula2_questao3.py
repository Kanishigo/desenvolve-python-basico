# Solicitação e entrada dos dados
idade = int (input ("Digite sua idade: "))
experiencia = int (input ("Digite quantos jogos de tabuleiro você já jogou: "))
vitoria = int (input ("Digite quantas vitórias possui: "))

# Validação das condicionantes
idade_torneio = (idade >= 16) and (idade <= 18)
exp = (experiencia >= 3)
vit = (vitoria >= 1)

# Impressão do resultado
print (f"Apto para ingressar no clube de jogos de tabuleiro: {idade_torneio and exp and vit}")