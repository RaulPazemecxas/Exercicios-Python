#crie um programa que leia o nome de sete pessoas e falem se são maiores ou menores de idade
from datetime import date

at = date.today().year
totmaior = 0
totmenor = 0

for pessoas in range(1, 8):
    nas = int(input("Digite o ano de nascimento da {}: ".format(pessoas)))
    idade = at - nas
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print("ao todo tivemos {} pessoas maiores de idade ".format(totmaior))
print("ao todo tivemos {} pessoas menores de idade".format(totmenor))
