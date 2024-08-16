import random

marido=['joão', 'josé', 'paulo', 'luiz', 'claudio']
esposas=['maria', 'carla', 'sueli', 'jurizcleide', 'monalisa']
random.seed()
x = random.randint(0,4)
n = int(input('Escolha seu sexo 1-Homen e 2-Mulher e pressione [ENTER]:'))
print('Número sorteado',x)

if n == 1:
    print('Você vai se casar com a',esposas[x])

elif n == 2:
    print('Você vai se casar com a',marido[x])

else:
    print('Você não vai se casar')

