frase = input ("Digite uma frase: ")

for vogal in frase:
    if vogal in "aeiouAEIOU":
        frase.replace(vogal, "*")

print (frase)
