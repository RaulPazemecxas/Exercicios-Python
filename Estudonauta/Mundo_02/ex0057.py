# Validação de dados (MASCULINO/FEMININO)

while True:
    sexo = str(input("Digite seu sexo (UTILIZE M OU F): [M / F]   ")).isupper()
    if sexo != 'M' and sexo != 'F':
        print("Digite um sexo valido")

    else:
        break
        pass
