url = ['www.google.com','www.gmail.com', 'www.github.com', 'www.reddit.com', 'www.yahoo.com' ]
dominio = []

for i in range (len(url)):
#    print ("iteração: ", i)
    endereco = []
    endereco = list(url[i])
#    print (endereco)
    del endereco[0:4]
#    print ("endereco sem 'www.': ", endereco)
    del endereco[:len(endereco)-5:-1]
#    print ("endereco sem '.com': ", endereco)
    dominio.append(''.join(endereco))
#    print (i, dominio[i])

print(dominio)
