#desafio computador x pessoa

import random
import time
from tqdm import tqdm

print("\033[40m#"*20, "\U0001f600 Seja bem-vindo ao jogo HOMEM X COMPUTER \U0001f600", "#\033[40m"*20)

print("""\033[31m\nREGRAS\033[31m: 
    \n-O computador irá pensar em um número, inteiro, de 0 a 10. 
    \n-Você tem que advinhar qual número ele escolheu!\033[0;0m\033[40m\n""")

for i in tqdm(range(0, 100), desc="\033[1m\033[40m=-=-=- 🖥: Olá! Eu sou o PC, estou pensando em um número, aguarde"):
    time.sleep(0.1)

while True:
    pc = random.randint(0, 10)
    numero_escolhido = int(input("\033[1m\nDigite o número escolhido pelo PC:      \033[0;0m"))

    if numero_escolhido == pc:
        print("\033[40m🖥: Fui derrotado, você acertou :(")
        break
        pass
    else:
        print("\033[40m🖥: Errou! Eu pensei no número {}, tente novamente.".format(pc))


