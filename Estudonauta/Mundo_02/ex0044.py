#calculadora de formas de pagamento

p = float(input("Preço das compras: "))
print(""""FORMAS DE PAGAMENTO
[1]A VISTA
[2] A VISTA CARTAO
[3] 2X NO CARTAO
[4] 3X OU MAIS NO CARTAO""")

if p == 1:
    total = (p*10/100)
elif p == 2:
    total = (p*5/100)
elif p == 3:
    total = p
elif p == 4:
    total = (p*20/100)
else:
    print("digite uma das opções acima")

