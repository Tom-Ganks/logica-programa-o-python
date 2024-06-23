'''
Escreva um algoritmo que receba a idade de 10 pessoas, calcule e imprima a
quantidade de pessoas maiores de idade (idade >= 18 anos).
'''

idades = 0

for idade in range(1, 11):
    idade = float(input("Digite a idade da pessoa {idade}: "))

    if idade >= 18:
     idades += 1

print(f"Quantidade de pessoas maiores de idade: {idades}")