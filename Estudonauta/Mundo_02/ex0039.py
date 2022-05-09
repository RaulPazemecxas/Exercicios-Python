#faça um programa que leia o ano de nascimento de um jovem e informe:#de acordo com sua idade sele ainda vai se alistar
#serviço militar, se é a hora de se alistar ou se ja passou do tempo dele se alistar, seu programa deve mostrar
#também o tempo que falta ou o quanto passou do prazo para o alistamento.

from datetime import date
from tqdm import tqdm
import time

while True:
    atual = date.today().year

    print("")
    print("#"*15, """ 👮 SEJA BEM VINDO AO PROGRAMA DE ALISTAMENTO MILITAR 👮""", "#"*15)
    inicio = str(input("\nOlá, vamos iniciar o calculo do alistamento?: [S] ✔️ PARA SIM [N] ❌ PARA NÃO: ")).upper()
    if inicio == "S":
        while True:
            try:
                nome = str(input("\nCerto, vamos iniciar. Qual seu nome completo?: "))
                nomev = nome.isdigit()


                if nomev == True:
                    print("Digite um nome valido")
                else:
                    while True:
                        idade = int(input(" {}, qual sua idade?: ".format(nome.split()[0])))
                        break
            except ValueError:
                print("\n\nDigite um nome e idade válidos!")
            break
    elif inicio == "n":

        exit()

    else:
        print("\n", "#"*15,"Valor invalido! Digite S ou N!","#"*15)

    print("""\n\nCerto! carregando módulos do programa
    
            """)

    for i in tqdm(range(0, 100), desc="Aguarde, {}! Estamos avaliando".format(nome)):
        time.sleep(0.1)
    break
if idade == 18:
    print("Você deve se alistar imediatamente!")
elif idade < 18:
     print("Ainda resta(m) {} ano(s) para você se apresentar".format(18 - idade))
elif idade > 18:
        print("Você deveria ter se alistado hà {} ano(s)".format(idade - 18))
else:
    print("Erro")

print("Data atual: ", atual)

