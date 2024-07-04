def validador (senha):
    
    return (not senha.islower() and len(senha) >= 8 and not senha.isalpha() and not senha.isalnum())

senha = input("Digite sua senha : ")

print (validador(senha))
