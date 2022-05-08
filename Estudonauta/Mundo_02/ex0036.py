import re
from tqdm import tqdm
import time


while True:
    print("\n", "=-=-="*5,  "  Seja bem-vindo ao simulador de financiamento!  \U0001F600  ", "=-=-="*5)
    while True:
        try:
            nome = input("\n\nVamos iniciar a analise do seu crédito, por favor, digite seu nome completo:  ")
            nomev = any(chr.isdigit() for chr in nome)
            if nomev == True:
                print()
                print("-"*20,"Por favor, digite um nome valído!","-"*20)
            else:
                break
        except Exception:
            print("Por favor, digite um nome valído!")

    print("\nCerto,{}, responda o seguinte questionário abaixo:\n".format(nome.upper()))
    print(80*"--")

    while True:
        try:
            renda = float(input("\nRenda mensal: "))
            credito = float(input("\nValor do crédito solicitado: "))
            pass
            break
        except ValueError:
            print("Digite um valor númerico e utilize ponto para números quberados!")

    while True:
        try:
            anos = int(input("\nEm quantos anos pretende pagar o crédito?  "))
            max = 5
            if anos > max:
                print(
                    "\n \U0001F4A1 Não possuimos linhas de crédito com esse tempo de pagamento, tente {} anos ou "
                    "menos \U0001F4A1 ".format(max))
            else:
                pass
                break
        except ValueError:
            print("\nDigite um valor inteiro e númerico, se o número for quebrado utilize ponto ao invés de virgulas!")


    minimo = (30 / 100) * renda
    presta = credito / (12 * anos)
    nomeregex = re.sub(r"\s+", "", nome)

    time.sleep(0.2)

    print("PROCESSANDO... \U0001F4BB")
    for i in tqdm(range(0, 100), desc ="Aguarde, {}! Estamos avaliando seu pedido".format(nome)):
        time.sleep(0.1)
    if presta <= minimo:
        print("\nBoas nóticias! Seu crédito foi aprovado! \u2713 ")
    else:
        print("\nInfelizmente, sua solicitação foi negada!")
        time.sleep(0.4)