#calculo de IMC

massa = float(input("Qual seu peso?"))
altura = float(input("Digite sua altura"))
imc = massa / (altura ** 2)
print(imc)

if imc < 18.5:
    print("Abaixo")
elif imc <= 18.5 and imc < 25:
    print("ideal")
elif imc <= 30 and imc >= 25:
    print("sobre")
elif imc > 30 and imc <= 40:
    print("Obse")
elif imc >=40:
    print("morb")