'''2. Crie uma classe chamada produto. 
Defina os seguintes atributos: código, nome, preço, quantidade.
Crie um algoritmo para cadastro de produtos. 
Faça com que seja possível fazer a busca do produto pelo código. 
Imprima os dados do produto.
parte 2  Crie método na classe produto chamado desconto, onde deve passar com parâmetro o percentual de desconto e retorne o preço com desconto.
Crie outro método na classe produto chamado reajuste, onde deve passar com parâmetro o percentual de acréscimo e retorne o preço reajustado. '''


class produto:

    def __init__(self, codigo='', nome='', preço='', quantidade=[]):
        self.codigo = codigo
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade


    produto = []
    while True:
        codigo = input("Digite o código do produto: ")
        if codigo == "":
            break
        nome = input("Digite o nome do produto: ")
        preço = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        produto.append(produto(codigo, nome, preço, quantidade))
        print("Produto cadastrado com sucesso!")
        print("\nDeseja cadastrar outro produto? (S/N)")
        
    




