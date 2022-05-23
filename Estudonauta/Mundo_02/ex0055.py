
somaidade = 0

for p in range(1, 5):
    print("---{} PESSOA------".format(p))
    nome = str(input("digite o nome da {} pessoa:  ".format(p)))
    idade = int(input("Digite a idade da {}: ".format(nome)))
    sexo = str(input("Digite o sexo (M / F): ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
        print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))

media = somaidade / 4
print("A media do grupo é de {}".format(media))
print("O homem mais velho tem {} e seu nome é {} ".format(maioridadehomem, nomevelho))

