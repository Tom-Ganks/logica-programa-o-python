from .pizza_especial import PizzaEspecial

class Pedido:
    def __init__(self, numero_pedido: int):
        self.pizzas = []
        self.numero_pedido = numero_pedido
            
    def adicionar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def total_pedido(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.preco
            if isinstance(pizza, PizzaEspecial):
                total += pizza.calcular_adicional()
        return total
    
    def detalhes_pedido(self):
        print('\n ##### Itens do pedido #####')
        for pizza in self.pizzas:
            pizza.detalhes()
            if isinstance(pizza, PizzaEspecial):
                pizza.detalhes_especiais()
            print('')
        print(f'Total do Pedido #{self.numero_pedido}: R${self.total_pedido():.2f}')
        print('')
    
# Instanciando as pizzas
# pizza1 = Pizza('Calabresa', 'M')
# pizza1.calcular_preco()

# pizza2 = Pizza('Portuguesa', 'G')
# pizza2.calcular_preco()

# pizza3 = PizzaEspecial('Calabresa', 'M', ['Muçarela', 'Cheddar'])
# pizza3.calcular_preco()

# # Criando um pedido
# p = Pedido(1010)
# p.adicionar_pizza(pizza1)
# p.adicionar_pizza(pizza2)
# p.adicionar_pizza(pizza3)

# # Exibindo detalhes das pizzas no pedido
# for pizza in p.pizzas:
#     pizza.detalhes()
#     if isinstance(pizza, PizzaEspecial):
#         pizza.detalhes_especiais()

# # Exibindo o total do pedido
# p.detalhes_pedido()
