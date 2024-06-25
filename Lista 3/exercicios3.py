def tab(number):
    print(f"Tabuada do {number} : ")

    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

number = int(input("Digite um número de tabuada: "))
tab(number)
