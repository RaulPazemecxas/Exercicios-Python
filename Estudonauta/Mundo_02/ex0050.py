#desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares
#se o valor for impar, desconsidere-0
s = 0
cont = 0

for c in range(1, 7):
    num = int(input("Digite {} numero inteiro".format(c)))
    if num % 2 == 0:
        s = s + num
        cont = cont + 1
print(cont, s)
