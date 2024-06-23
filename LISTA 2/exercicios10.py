contador = 0
contF = 0
contM = 0
mediaF = 0.0
mediaM = 0.0
maior = 0
menor = 0

qtde = int(input('Digite a quantidade de Homens ou Mulheres:'))

while contador < qtde:
    sexo = input('Digite o sexo: ')
    altura = float(input('Digite a altura: '))

    if altura > maior:
        maior = altura

    if altura > menor:
        menor = altura

    if sexo.upper() == 'F':
        contF = contF + 1
        mediaF = mediaF + altura
    elif sexo.upper() == 'M':
        contM = contM + 1
        mediaM = mediaM + altura
    else:
        print('Sexo inválido')
        continue
    contador = contador + 1

print('Quantidade de alunos do sexo feminino: ', contF)
print('Quantidade de alunos do sexo masculino: ', contM)

if contF > 0:
    mediaF = mediaF / contF

if contM > 0:
    mediaM = mediaM / contM # média e a soma dos valores dividido pela quantidade.

print('Média de altura das mulheres: ', mediaM)
print('Média de altura dos homens: ', mediaF)

print('Maior altura do grupo é: ', maior)
print('Menor altura do grupo é: ', menor)