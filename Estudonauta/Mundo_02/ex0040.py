#Crie um programa que leia duas notas de um aluno e calcule a sua média:
#mostrando uma mensagem no final de acordo com a média atingida:
#- abaixo de 5 : reprovado
#- entre 5 e 6.9\; recuperação
#- 7 ou superior: aprovado

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
mn = (n1 + n2) / 2

if mn < 5.0:
    print("REPR")
elif mn == 5.0 or mn <= 6.9:
    print("REC")
else:
    print("APRO")