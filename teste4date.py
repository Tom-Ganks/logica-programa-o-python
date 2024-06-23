from datetime import date
data_atual = date.today()
ano_nascimento= int(input("Ano de nascimento:"))
ano_atual = data_atual.year
idade =ano_atual-ano_nascimento
print('\n')
print('Neste ano sua idade será ',idade,' anos')