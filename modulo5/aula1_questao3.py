import random

aux = random.randint(1,10)
while True:
    n = int (input ("Digite um número inteiro: "))
    if n == aux:
        print ("Parabéns! Vocè acertou!")
        break
    if n > aux:
        print ("Muito alto.")
    else:
        print ("Muito baixo.")