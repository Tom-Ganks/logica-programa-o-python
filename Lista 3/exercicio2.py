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
