#gerador de PA

primeiro = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end='')
    termo = termo + raz
    cont = cont + 1
