
class Aluno:

    def __init__(self, nome='', matricula='', notas=[]):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
        self.media = 0
        self.conceito = ''
        self.resultado = ''
        self.resultado = ''

    def conceito_aluno(self):
        if self.media < 4:
            return 'E'
        elif self.media < 6:
            return 'D'
        elif self.media < 75:
            return 'C'
        elif self.media < 90:
            return 'B'
        else:
            return 'A'

    def resultado_aluno(self):
        if self.conceito == 'A' or self.conceito == 'B' or self.conceito == 'C':
            return 'Aprovado'
        else:
            return 'Reprovado'

    def impressao(aluno):
        print(f'Matricula: {aluno.matricula}')
        print(f'Aluno: {aluno.nome}')
        print(f'Notas: {aluno.notas}')
        print(f'Media: {round(aluno.media, 1)}')
        print(f'Conceito: {aluno.conceito}')
        print(f'Resultado: {aluno.resultado}')

alunos = []
while True:
    nome = input('Digite o nome do aluno: ')
    matricula = input('Digite a data da matrícula: ')
    notas = []

    for i in range(3):
        nota = float(input(f'Digite a {i+1}ª nota do aluno: '))
        notas.append(nota)
    aluno = Aluno(nome, matricula, notas)
    aluno.media = sum(aluno.notas) / len(aluno.notas)
    aluno.conceito = aluno.conceito_aluno()
    aluno.resultado = aluno.resultado_aluno()
    aluno.append(aluno)

    sair = input('Digite s para sair ou enter para continuar: ')

    if sair.lower() == 's':
        break

def impressao(aluno):
    print(f'Matricula: {aluno.matricula}')
    print(f'Aluno: {aluno.nome}')
    print(f'Notas: {aluno.notas}')
    print(f'Media: {round(aluno.media, 1)}')
    print(f'Conceito: {aluno.conceito}')
    print(f'Resultado: {aluno.resultado}')

#aluno1 = Aluno(nome='Matheus', matricula='2023', notas=[8, 8, 8])
#aluno1.media = sum(aluno1.notas) / len(aluno1.notas)
#aluno1.conceito = aluno1.conceito_aluno()
#aluno1.resultado = aluno1.resultado_aluno()

#aluno2 = Aluno(nome='Gabriel', matricula='2023', notas=[6.5, 4, 3])
#aluno2.media = sum(aluno2.notas) / len(aluno2.notas)
#aluno2.conceito = aluno2.conceito_aluno()
#aluno2.resultado = aluno2.resultado_aluno()

for aluno in alunos:
    impressao(aluno)
    print('')

busca = input('Digite a matrícula do aluno desejado: ')

achei_aluno = ''
for aluno in alunos:
    if busca == aluno.matricula:
        achei_aluno = aluno.matricula
        break
if achei_aluno != '':
    impressao(aluno)
else:
    print('Matricula não encontrada.')