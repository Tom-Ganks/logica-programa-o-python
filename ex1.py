nota1 = float(input('digite a nota 1: '))
nota2 = float(input('digite a nota 2: '))

media = (nota1 + nota2) / 2

if media >= 6:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')