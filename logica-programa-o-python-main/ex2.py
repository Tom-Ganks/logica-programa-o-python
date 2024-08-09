altura = float(input('digite sua altura: '))
sexo = input('digite seu sexo: ')
def calcularPeso_Ideal(altura, sexo):
    if sexo == "Masculino":
        pesoIdeal = (72.7 * altura) - 58
    elif sexo == "Feminino":
        pesoIdeal = (62.1 * altura) - 44.7
    else:
        print ('sexo inválido')
        return None
    return pesoIdeal

# parte 2

peso = float(input('seu peso: '))

imc = peso / (altura ** 2)
print("Seu imc é", imc, "quilos")

if imc < 18.5:
    print('Abaixo do peso')
    
elif 18.5 <= imc <= 25:
    print('Peso normal')

elif 25 <= imc <= 30:
    print('Sobrepeso')

elif 30 <= imc <= 35:
    print('Obesidade grau 1')

elif 35 <= imc <= 40:
    print('Obesidade grau 2')

else:
    print('Obesidade grau 3')


