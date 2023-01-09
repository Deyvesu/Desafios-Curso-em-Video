nome = (input("Digite seu nome: "))

print("Só tem espaços? ", nome.isspace())
print("Só tem números? ", nome.isnumeric())
print("Tem números ou letras? ", nome.isalnum())
print("Está em maiúsculo? ", nome.isupper())
print("Está em minuúsculo? ", nome.islower())
print("Está capitalizada? ", nome.istitle())


