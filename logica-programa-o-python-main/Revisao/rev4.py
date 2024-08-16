'''Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de aproveitamento, usando a fórmula: 
MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME) / 7 
Crie uma função para o cálculo.
A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E. 
Média de aproveitamento Conceito 
>= 90 A 
>= 75 e < 90 B 
>= 60 e < 75 C 
>= 40 e < 60 D 
< 40 E'''

def conceito(ma):
    if ma < 40:
        return 'E'
    elif ma < 60:
        return 'D'
    elif ma < 75:
        return 'C'
    elif ma < 90:
        return 'B'
    else:
        return 'A'
    
def resultado(conceito):
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        return 'Aprovado'
    else:
        return 'Reprovado'
try:
    matricula = input('Digite a matricula: ')
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))
    me = float(input('Digite a média de exércícios: '))
    ma = (nota1 + nota2 * 2 + nota3 * 3 + me) /7
    print('\n################## Resultados ###################')
    print(f'Matrícula: {matricula}')
    print(f'Nota 1: {nota1} | Nota 2: {nota2} | Nota 3: {nota3} | ME: {me}')
    print(f'Média de aproveitamento MA: {ma}')
    print(f'Conceito: {conceito(ma)}')
except Exception as e:
    print(f'Ocorreu o seguinte erro: {e}')
    