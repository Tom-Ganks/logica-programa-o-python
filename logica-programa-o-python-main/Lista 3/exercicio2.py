<<<<<<< HEAD
Q = []
P = []
total = 0
vendas = int(input("Digite a quantidade de venda: "))

for i in range(vendas):
    quant = int(input("Digite a quantidade de mercadorias vendidas{i}: "))
    preco = float(input("Digite o preço das mercadorias vendidas{i}: "))
    Q.append(quant)
    P.append(preco)
    total += quant * preco

print(f"Lista de quantidades: {Q:.2f}")
print(f"lista dos precos: {P:.2f}")

print(f"O faturamento mensal é de: {total}")
=======
Q = []
P = []

for i in range(10):
    Quantidade = int(input("Digite a quantidade de mercadorias vendidas{i}: "))
    preco = float(input("Digite o preço das mercadorias vendidas{i}: "))
    Q.append(Quantidade)
    P.append(preco)

    if len(Q) != len(P):
        print("Erro: As listas Q e P devem ter o mesmo comprimento.")


    faturamento = 0.0
    for i in range(10):
        faturamento = faturamento + (Q[i] * P[i])

        print(f"O faturamento total é R$: {faturamento}")
>>>>>>> 275cba4d39bb3b4df361b0ad2021c2b179d3c4da
