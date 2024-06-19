idade = int(input('digite sua idade'))

if 18 <= idade <= 65:
    print('Eleitor Obrigatorio')
elif 16 <= idade <= 65:
    print('Eleitor facultativo')
else:
    print('Não é eleitor')