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