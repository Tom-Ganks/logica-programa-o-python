from .pizza import Pizza

class PizzaEspecial(Pizza):
    def __init__(self, nome: str, tamanho: str, adicionais: list):
        super().__init__(nome, tamanho)
        self.adicionais = adicionais
    
    def calcular_adicional(self):
        preco_adicional = 2
        total = 0
        for item in self.adicionais:
            total += preco_adicional
        
        return total
    
    def detalhes_especiais(self):
        print(f'Adicionais: {self.adicionais}')
        print(f'Preço dos adicionais: R${self.calcular_adicional():.2f}')
    
# pizza = PizzaEspecial('Calabresa', 'M', ['Muçarela', 'Chedder'])

# pizza.calcular_preco()

# pizza.detalhes()
# pizza.detalhes_especiais()