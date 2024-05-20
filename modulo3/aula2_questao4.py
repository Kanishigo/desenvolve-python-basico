# Solicitação e entrada dos dados
classe = input ("Digite a classe (guerreiro, mago ou arqueiro): ")
forca = int (input ("Digite os pontos de força (de 1 a 20): "))
magia = int (input ("Digite os pontos de magia (de 1 a 20): "))

# Validação das condicionantes
guerreiro = (classe == "guerreiro") and (forca > 14) and (magia < 11)
mago = (classe == "mago") and (forca < 11) and (magia > 14)
arqueiro = (classe == "arqueiro") and ((forca and magia) > 5) and ((forca and magia) < 16)

# Impressão dos resultados
print (f"Pontos de atributo consistentes com a classe escolhida: {guerreiro or mago or arqueiro}")