
# 1 tentativa falha
'''class Pizza:
    def __init__(self, nome, tamanho, preco):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = preco
        self.adicionar_adicional = []


    def calcular_preco(self):
        if self.tamanho == 'Pequena':
            return self.preco
        elif self.tamanho == 'Média':
            return self.preco + 1
        elif self.tamanho == 'Grande':
            return self.preco + 2
        else:
            return 'Tamanho inválido'
        

    def adicionar_adicional(self, adicional):
        self.adicionar_adicional.append(adicional)
        self.preco += 1


    def exibe_detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Tamanho: {self.tamanho}')
        print(f'Preço: {self.preco}')
        print(f'Adicionais: {self.adicionar_adicional}')


class PizzaEspecial(Pizza):
    def __init__(self, nome, tamanho, preco, adicionais):
        super().__init__(nome, tamanho, preco)
        self.adicionais = adicionais

    def calcular_preco(self):
        super().calcular_preco()
        for adicional in self.adicionais:
            self.adicionar_adicional(adicional)
            self.preco += 1

    def exibe_detalhes(self):
        super().exibe_detalhes()
        print(f'Adicionais Especiais: {self.adicionais}')
        

class Pedido:
    def __init__(self):
        self.pizzas = []
        self.numero_pedido = self.gerar_numero_pedido()
        self.total = 0

    def gerar_numero_pedido(self):
        import random
        return random.randint(1000, 9999)
    
    def adicionar_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total += pizza.calcular_preco()
'''

# 2 tentativa(quase feito)... (As partes em que usei join foi algo pesquisado no google como nao consegui consertar o codigo tive de pesquisar.)
class Pizza:
    def __init__(self, nome, tamanho, preco):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = preco

    def calcular_preco_final(self): #apenas essa função que usei IA para arredondar todos os tamanhos numa função só, mas não sabia como.
        multiplicadores = {
            'Pequena': 1.0,
            'Média': 1.2,
            'Grande': 1.5
        }
        return self.preco * multiplicadores.get(self.tamanho, 1.0) #get foi algo que vi breviamente na plataforma rocketseat, anos atrás... ele que pega o tamanho na função

    def mostrar_detalhes(self):
        preco_final = self.calcular_preco_final()
        return (f"Pizza: {self.nome}\n"
                f"Tamanho: {self.tamanho}\n"
                f"Preço Base: R${self.preco:.2f}\n" # 2f parte que aprendi em um tutorial no youtube em casa , arredonda para 2 numeros f = float
                f"Preço Final: R${preco_final:.2f}") # 2f parte que aprendi em um tutorial no youtube em casa , arredonda para 2 numeros f = float

class PizzaEspecial(Pizza):
    def __init__(self, nome, tamanho, preco, adicionais):
        super().__init__(nome, tamanho, preco)
        self.adicionais = adicionais

    def calcular_preco_final(self):
        preco_final = super().calcular_preco_final()
        custo_adicionais = len(self.adicionais) * 2.0  # Cada adicional custa R$2.00
        return preco_final + custo_adicionais

    def mostrar_detalhes(self):
        detalhes = super().mostrar_detalhes()
        adicionais_str = ", ".join(self.adicionais)
        return (f"{detalhes}\n"
                f"Adicionais: {adicionais_str}")

class Pedido:
    def __init__(self, numero_pedido):
        self.pizzas = []
        self.numero_pedido = numero_pedido

    def adicionar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calcular_total(self):
        return sum(pizza.calcular_preco_final() for pizza in self.pizzas)

    def mostrar_detalhes(self):
        detalhes_pizzas = "\n\n".join(pizza.mostrar_detalhes() for pizza in self.pizzas)
        return (f"Pedido Número: {self.numero_pedido}\n\n"
                f"{detalhes_pizzas}\n\n"
                f"Total do Pedido: R${self.calcular_total():.2f}") # ():.2f parte que aprendi em um tutorial no youtube em casa

# Testando o código
if __name__ == "__main__":
    # Criando algumas pizzas
    pizza_margherita = Pizza("Margherita", "Média", 30.00)
    pizza_calabresa = PizzaEspecial("Calabresa", "Grande", 35.00, ["Azeitona", "Cebola", "Pimentão"])

    # Criando um pedido
    pedido1 = Pedido(101)
    pedido1.adicionar_pizza(pizza_margherita)
    pedido1.adicionar_pizza(pizza_calabresa)

    # Exibindo detalhes do pedido
    print(pedido1.mostrar_detalhes())

    print(pedido1.exibir_detalhes())
