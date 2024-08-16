'''
pesquisa senac com os alunos: 5
1-Quantidade de alunos do sexo feminino
2-Quantidade de alunos do sexo Masculino
3-Média de altura dos alunos do sexo Feminino
4-Média de altura dos alunos do sexo Masculino
5-Aluno com maior altura
6-Menor

'''
contF = 0
contM = 0
mediaF = 0.0
mediaM = 0.0
maior = 0
menor = 99
for n in range(0,5):
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
    

print('Quantidade de alunos do sexo feminino: ', contF)
print('Quantidade de alunos do sexo masculino: ', contM)

if contF > 0:
    mediaF = mediaF / contF

if contM > 0:
    mediaM = mediaM / contM # média e a soma dos valores dividido pela quantidade.

print('Média de altura dos alunos do sexo feminino: ', mediaF)
print('Média de altura dos alunos do sexo masculino: ', mediaM)

print('Aluno com maior altura: ', maior)