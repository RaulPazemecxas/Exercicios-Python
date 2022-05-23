#desenvolva um programa que leia o primeiro termo e a razão de uma PA no ginal mostre os 10 priomeiros termos dessa PA

primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print(c)