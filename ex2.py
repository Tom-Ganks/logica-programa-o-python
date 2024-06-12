altura = float(input('digite sua altura: '))
sexo = input('digite seu sexo: ')

if sexo == "Masculino":
    pesoIdeal = (72.7 * altura) - 58
elif sexo == "Feminino":
    pesoIdeal = (62.1 * altura) - 44.7
else:
    pesoIdeal = ("Attack Helicopter")
print('Seu peso ideal é', sexo, round(pesoIdeal, 2), "quilos")