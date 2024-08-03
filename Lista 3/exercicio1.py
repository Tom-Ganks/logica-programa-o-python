<<<<<<< HEAD
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

numbers = [int(numeros) for numeros in numbers]

maior_numero = numbers[0]
indice_maior = 0

for i in range(1, len(numbers)):
    if numbers[i] > maior_numero:
        maior_numero = numbers[i]
        indice_maior = i

print(f"O maior número é {maior_numero} e está no índice {indice_maior}.")
=======
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

numbers = [int(numeros) for numeros in numbers]

maior_numero = numbers[0]
indice_maior = 0

for i in range(1, len(numbers)):
    if numbers[i] > maior_numero:
        maior_numero = numbers[i]
        indice_maior = i

print(f"O maior número é {maior_numero} e está no índice {indice_maior}.")
>>>>>>> 275cba4d39bb3b4df361b0ad2021c2b179d3c4da
