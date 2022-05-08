#Escreva  um programa que leia um número inteiro qualquer e peça para o usuario escolher qual sera a nase
#de conversão: binario / octal / hexadecimal

print("#"*30,"Seja bem vindo à calculadora de binários, octais e hexadecimais! 🕹 ️", "#"*30)
print("\n- A calculadora realiza a conversão de números inteiros, para as opções apresentadas!")
print("""
##### USO  #####

-Digite o número, inteiro e sem virgulas, que deseja converter!
-Não utilize números quebrados, e cuidado no preenchimento das informações!
""", )
while True:
    try:
        num = int(input("Digite um número inteiro qualquer: "))
        break
        pass
    except ValueError:
        print("\n\nDigite um número inteiro, sem uso de virgulas e letras!")

print("""Você deseja converter para qual base? 🔎: 

    ####### [1] binário 
    ####### [2] octal  
    ####### [3] hexadecimal 
    """)
while True:
        try:
            escolha = str(input("Digite a opção: "))
            if escolha == "1" or escolha == "2" or escolha == "3":
                pass
                break
            else:
                print("Digite as opções entre 1, 2 ou 3, por favor! 🙃")

        except ValueError:
                print("Digite um valor entre as 3 opções apresentadaas! 🙃")

if escolha == "1":
    print("{} ".format(bin(num)[2:]))

elif escolha == "2":
    print("{}".format(oct(num)[2:]))

elif escolha == "3":
    print("{}".format(hex(num)[2:]))
    print("")

else:
    print("\nOpção invalida!")





