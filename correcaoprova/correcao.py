class Pizza:
    def __init__(self, nome: str, tamanho: str,):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = 0.0

    def calcular_preco(self):
        tamanho_preco = {
            'P': 10,
            'M': 20,
            'G': 30
        }
        self.preco = tamanho_preco.get(self.tamanho)

    def detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Tamanho: {self.tamanho}')
        print(f'Preco: {self.preco}')

class PizzaEspecial(Pizza):
    def __init__(self, nome: str, tamanho: str, adicionais: list):
        super().__init__(nome, tamanho)
        self.adicionais = adicionais

    def calcular_adicionais(self):
        preco_adicional = 2
        total = 0
        for item in self.adicionais:
            total += preco_adicional

        return total
    
    def detalhes_especiais(self):
        print(f'Adicionais: {self.adicionais}')
        print(f'Preço dos adicionais: {self.calcular_adicionais()}')

# Pizza = PizzaEspecial('Calabresa', 'M', ['Muçarela', 'Chedder'])

# Pizza.calcular_preco()

# Pizza.detalhes()
# Pizza.detalhes_especiais()

class Pedido:
    def __init__(self, numero_pedido: int):
        self.pizzas = []
        self.numero_pedido = numero_pedido

    def adicionar_pizza(self, pizza,):
        self.pizzas.append(pizza)
        
    def total_pedido(self):
        total = 0
        for pizza in self.pizzas:
            if isinstance(pizza, PizzaEspecial):
                pizza.detalhes_especiais()

        return total
    
    def detalhes_pedido(self):
        print(f'Total do pedido: {self.numero_pedido()}: R${self.total_pedido():2f}')
    
pizza1 = Pizza('Calabresa', 'M')
pizza1.calcular_preco()

pizza3 = Pizza('Portuguesa', 'G')
pizza3.calcular_preco()

p = Pedido(1010)
p.adicionar_pizza(pizza1)

p.adicionar_pizza(pizza3)


for pizza in p.pizzas:
    pizza.detalhes()
    if isinstance(pizza, PizzaEspecial):
        pizza.detalhes_especiais()

p.detalhes_pedido()

lista_pizzas = ['Calabresa', 'Portuguesa', 'Napolitana']
lista_adicionais = ['Mucarela', 'Chedder', 'Ovo', 'Bacon', 'Peperroni']
print('''
      Preçoes: P - 10, M - 20, G - 30
      1 - Calabresa 
      2 - Portuguesa
      3 - Napolitana
      ''')

op = int(input('Escolha a pizza: '))

tamanho = input('Tamanho [P, M, G]')

escolha = input('Deseja algum Adicional [S - Sim, N - Não]? ')

if escolha.upper() == 'S':
    while escolha.upper() == 'S':
        adicional = input('''Informe o Adicional:
                          1 - Mucarela
                          2 - Chedder
                          3 - Ovo
                          4 - Bacon
                          5 - Peperroni ''')
        if adicional:
             lista_adicionais.append(adicional)
             escolha = input('Deseja algum Adicional [S - Sim, N - Não]? ')
             pizza = PizzaEspecial(pizza[op-1], tamanho, adicional)
             pizza.calcular_preco
    else:
        pizza = Pizza(lista_pizzas[op-1], tamanho)
        pizza.calcular_preco()
        




