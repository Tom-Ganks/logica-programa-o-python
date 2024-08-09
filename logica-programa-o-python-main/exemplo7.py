'''
Algoritmo que armazena uma lista de nomes. o usuario
deve digitar os nomes até que seja informado -1
Mostrar o número de pessoas
Printar a lista em ordem alfabética
Printar o 3 elemento da lista
Realizar um sorteio e mostrar o nome do ganhador

'''
import random

nomes = []
while True:
    nome = input("Digite o nome (Digite -1 para parar): ")
    if nome == "-1":
        break
    else:
        nomes.append(nome)

num_pessoas = len(nomes)
print(f"O número de pessoas é: {num_pessoas}")

ordem_nomes = sorted(nomes)
print("Lista de nomes em ordem alfabetica")
for nome in ordem_nomes:
    print(nome)

if num_pessoas >=3:
    print(f"O terceiro nome da lista é: {ordem_nomes[2]}")
else:
    print("A lista não possui um terceiro elemento")

if num_pessoas >0:
    ganhador = random.choice(nomes)
    print(f"O ganhador é: {ganhador}")
else:
    print("A lista não possui esse nome")
