import random

num_elementos = random.randint(5,20)
elementos = []
for i in range(num_elementos):
    elementos.append(random.randint(1,10))

soma = sum(elementos)
tamanho = len(elementos)

print (num_elementos)
print (elementos)
print (soma)
print (soma/tamanho)