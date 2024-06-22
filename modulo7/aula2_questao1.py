meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
data_nasc = input ("Digite a data de nascimento (dd/mm/aaaa): ")

lista_nasc = data_nasc.split("/")
idx_mes_nasc = int(lista_nasc[1])-1

print ("Você nasceu em ", lista_nasc[0], " de ", meses[idx_mes_nasc], " de ", lista_nasc[2])
