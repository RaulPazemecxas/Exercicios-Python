#gerador de pa melhorado

primeiro = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= 10:
        print("{} -> ".format(termo), end='')
        termo = termo + raz
        cont = cont + 1
    print("PAUSA")
    mais = int(input("Quantos termos voce quer mostrar mais? "))
print("FIM")
