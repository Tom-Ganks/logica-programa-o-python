from datetime import datetime

nascimento = float(input("Digete seu ano de nascimento"))
ano_atual = float(input("Digite o ano atual"))

idade = ano_atual - nascimento

if idade > 0:
    idade = ano_atual - nascimento
    print(f"Você tem {idade} anos de idade")

else:
    (f"Seu ano de nascimento informado {nascimento} é inválido.")

