cont1= 0
cont2= 0
cont3= 0
cont0 = 0
cont4 = 0

while True:
    voto = int(input("Digite seu voto(1, 2, 3 - para candidatos, 0 para branco e 4 para nulo)"))

    if voto == 1:
        cont1 += 1 # cont1 = cont1 + 1
    elif voto == 2:
        cont2 += 1
    elif voto == 3:
        cont3 += 1
    elif voto == 0:
        cont0 += 1
    elif voto == 4:
        cont4 += 1
    elif voto == -1:
        break
    else:
        print("Voto inválido")

if cont1 > cont2 and cont2 > cont3:
    print("O vencedor é o {cont1}")

elif cont2 > cont1 and cont2 > cont3:
    print("O vencedor é o {cont2}")

else:
    print("O vencedor é o {cont3}")

print(f"o número de votos em branco é : {cont0}")

print(f"o número de votos nulos é : {cont4}")

print(f"o número de eleitores que compareceram as urnas: {cont0 + cont1 + cont2 + cont3 + cont4}")
