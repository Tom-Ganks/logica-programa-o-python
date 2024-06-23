numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2, 4, 6, 8, 10, 4, 5, 6, 7, 8, 9, 10, 11,]

def count_val(valor):
    count = 0

    for num in numbers:
        if num == valor:
            count += 1

    return count

numero = int(input("Digite no número para que conte quanta vezes ele aparece na lista: "))
quantidade = count_val(numero)
print(f"O número {numero} aparece {quantidade} vezes na lista.")