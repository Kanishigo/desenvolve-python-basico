import random

lista = []
id_fatia_maior, tam_fatia_maior = 0, 0
id_atual, tam_atual = 0, 0

for i in range(20):
    lista.append (random.randint(-10,10))

print (lista)

for i in range (20):
    print ("Inicio do laço: ", i, lista[i])
    if lista[i] < 0:
        tam_atual += 1
        print ("Maior fatia aumentou, ", tam_atual)
        if tam_atual == 1:
            print ("Inicio nova fatia. Indice: ", i)
            id_atual = i
    else:
        if tam_atual > tam_fatia_maior:
            print ("Maior fatia até agora", tam_atual)
            tam_fatia_maior = tam_atual
            id_fatia_maior = id_atual
        tam_atual = 0

print ("O indice da maior fatia inicia em: ", id_fatia_maior, " e tem tamanho = ", tam_fatia_maior)
del lista[id_fatia_maior:id_fatia_maior+tam_fatia_maior]
print (lista)