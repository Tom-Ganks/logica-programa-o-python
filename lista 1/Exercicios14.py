import math


a = float(input("Digite o número"))
b = float(input("Digite o próximo número"))
c = float(input("Digite o último número"))

if a == 0:
    print("impossivel realizar, coficiente deve ser difirente de zero")

else:
    delta = (b ** 2) - (4 * a * c)

    if delta >= 0:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        print(f"As ra´zes da equação são: x1 = {x1} e x2 = {x2}")
    else:
        print("Não há raízes. Delta é negativo")

    
