#crie um programa que leia doi valores  e mostre na tela a opção de somar multiplicar, ver o maior valor novos numeros
#e opção 5 sair do programa

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

op = 0

while op != 5:
    print("""    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚM.
    [ 5 ] SAIR DO MENU""")
    op = int(input(">>>>>Qual é a sua opção?"))
    if op == 1:
        soma = n1 + n2
        print("A soma entre os números {} e {} é igual a: {}".format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print("A multiplicação entre {} e {} é igual a: {}".format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print("Entre {] e {}, o maior valor é: {}".format(n1, n2, maior))
    elif op == 4:
        print("Informe os valores novamente: ")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif op == 5:
        print("Finalizadon..")

    else:
        print("Opção invalida")
