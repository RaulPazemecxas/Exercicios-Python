#a confederação de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
#de acordo com sua idade

from datetime import date

atual = date.today().year

ano = int(input("Digite o ano do seu nascimento: "))
idade = atual - ano
print("O atleta tem {} anos".format(idade))

if idade <= 9:
    print("mirim")
elif idade <= 14:
    print("infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 25:
    print("SENIOR")
else:
    print("Master")