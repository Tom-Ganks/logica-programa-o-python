<<<<<<< HEAD
'''
Escreva um algoritmo que receba a idade de 10 pessoas, calcule e imprima a
quantidade de pessoas maiores de idade (idade >= 18 anos).
'''

idades = 0

for idade in range(1, 11):
    idade = float(input("Digite a idade da pessoa {idade}: "))

    if idade >= 18:
     idades += 1

=======
'''
Escreva um algoritmo que receba a idade de 10 pessoas, calcule e imprima a
quantidade de pessoas maiores de idade (idade >= 18 anos).
'''

idades = 0

for idade in range(1, 11):
    idade = float(input("Digite a idade da pessoa {idade}: "))

    if idade >= 18:
     idades += 1

>>>>>>> 275cba4d39bb3b4df361b0ad2021c2b179d3c4da
print(f"Quantidade de pessoas maiores de idade: {idades}")