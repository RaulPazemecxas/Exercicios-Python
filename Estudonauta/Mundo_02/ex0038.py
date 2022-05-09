#escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# o primeiro valor é maior
#o segundo valor é maior
#nao existe valor maios, os dois sao iguais

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O PRIMEIRO valor é maior")
elif n1 < n2:
    print("O SEUGNDO valor é menor")
else:
    print("Os valores são iguais")