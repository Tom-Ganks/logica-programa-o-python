'''
Escreva um algoritmo que:
• leia um número indeterminado de linhas contendo, cada uma, a idade de um
indivíduo. A última linha, que não entrará nos cálculos, contém o valor da idade
igual a zero;
• calcule e escreva a idade média deste grupo de indivíduos.
'''

calculo_idade = 0
contagem = 0

print("Digite a idade do candidato (digite 0 para sair): ")

while True:
    idade = int(input("idade: "))

    if idade == 0:
        break

    calculo_idade += idade
    contagem += 1

    if contagem > 0:
        media_idade = calculo_idade / contagem
        print(f"A idade média do grupo de indivíduos é: {media_idade:.2f} anos")
    else:
        print("Nenhuma idade foi digida")
        
