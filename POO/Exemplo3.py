'''2. Crie uma classe chamada produto. 
Defina os seguintes atributos: código, nome, preço, quantidade.
Crie um algoritmo para cadastro de produtos. 
Faça com que seja possível fazer a busca do produto pelo código. 
Imprima os dados do produto.
parte 2  Crie método na classe produto chamado desconto, onde deve passar com parâmetro o percentual de desconto e retorne o preço com desconto.
Crie outro método na classe produto chamado reajuste, onde deve passar com parâmetro o percentual de acréscimo e retorne o preço reajustado. '''


class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

#codigo chat gpt para correção de erro (como resolver?)
#    def __str__(self):
#       return (f"Código: {self.codigo}\n"
#              f"Nome: {self.nome}\n"
#              f"Preço: R$ {self.preco:.2f}\n"
#              f"Quantidade: {self.quantidade}")

    def buscar_produto(codigo, lista_produtos):
        for produto in lista_produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        preco_com_desconto = self.preco - desconto
        return preco_com_desconto

    def reajuste(self, percentual):
        aumento = self.preco * (percentual / 100)
        preco_reajustado = self.preco + aumento
        return preco_reajustado


produtos = []
produtos.append(Produto(1, "Camiseta", 100.0, 10))
produtos.append(Produto(2, "Calça jeans", 150.0, 5))
produtos.append(Produto(3, "Tênis", 200.0, 20))


codigo_buscado = 2
produto_buscado = Produto.buscar_produto(codigo_buscado, produtos)

if produto_buscado:
    print("Produto encontrado: ")
    print(produto_buscado)

   
    percentual_desconto = 10  
    percentual_reajuste = 5   
    
    preco_com_desconto = produto_buscado.desconto(percentual_desconto)
    preco_reajustado = produto_buscado.reajuste(percentual_reajuste)
    
    print(f"\nPreço com desconto de {percentual_desconto}%: R$ {preco_com_desconto:.2f}")
    print(f"Preço com reajuste de {percentual_reajuste}%: R$ {preco_reajustado:.2f}")
    




