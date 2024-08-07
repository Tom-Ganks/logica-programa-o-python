class Aluno:

    def __init__(self, nome='', matricula='', notas=[]):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
        self.media = 0
        self.conceito = ''
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

aluno1 = Aluno(nome='Matheus', matricula='2023', notas=[8, 7 , 8])
aluno1.media = sum(aluno1.notas) / len(aluno1.notas)
aluno1.conceito = aluno1.conceito_aluno()
aluno1.resultado = aluno1.resultado_aluno()

print(f'Matricula: {aluno1.matricula}')
print(f'Aluno: {aluno1.nome}')
print(f'Notas: {aluno1.notas}')
print(f'Media: {round(aluno1.media, 1)}')
print(f'Conceito: {aluno1.conceito}')
print(f'Resultado: {aluno1.resultado}')