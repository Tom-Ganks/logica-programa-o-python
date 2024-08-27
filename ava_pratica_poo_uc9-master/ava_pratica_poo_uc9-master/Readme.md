**HABILITAÇÃO TÉCNICA DE NÍVEL MÉDIO EM INFORMÁTICA**

**Instrutor**: Wisner Antônio Marques

**Prova Prática de POO:  Sistema de Pizzaria**
```python
Objetivo: Implementar um sistema para gerenciar pedidos de uma pizzaria utilizando conceitos de Programação Orientada a Objetos, incluindo herança.
Instruções:
    1. Implemente as classes conforme especificado.
    2. Cada classe deve ter pelo menos um construtor (__init__) e métodos necessários para sua funcionalidade.
    3. Faça uso de herança entre as classes onde for necessário.
    4. Escreva exemplos de uso que demonstrem o funcionamento do sistema.
    5. Utilize boas práticas de programação, incluindo nomes de variáveis e métodos autoexplicativos e comentários onde necessário.
Descrição do Sistema:
Sua tarefa é criar um sistema simples para uma pizzaria que gerencie diferentes tipos de pizzas e seus pedidos. A pizzaria oferece pizzas tradicionais e especiais, e cada tipo de pizza pode ter diferentes tamanhos e adicionais.
Requisitos:
    1. Classe Pizza:
        ◦ Crie uma classe Pizza que tenha os seguintes atributos:
            ▪ nome: Nome da pizza (ex: Margherita, Calabresa).
            ▪ tamanho: Tamanho da pizza (ex: Pequena, Média, Grande).
            ▪ preco: Preço base da pizza.
        ◦ Adicione um método para calcular o preço final da pizza, considerando o tamanho.
        ◦ Adicione um método para exibir os detalhes da pizza.
    2. Classe PizzaEspecial (herda de Pizza):
        ◦ Crie uma classe PizzaEspecial que herde de Pizza.
        ◦ Adicione um atributo adicionais, que é uma lista de ingredientes extras.
        ◦ Modifique o método de cálculo de preço para adicionar um custo extra para cada adicional.
        ◦ Adicione um método para exibir os detalhes da pizza especial, incluindo os adicionais.
    3. Classe Pedido:
        ◦ Crie uma classe Pedido que gerencie um pedido de pizzas.
        ◦ A classe deve ter os seguintes atributos:
            ▪ pizzas: Uma lista de pizzas no pedido.
            ▪ numero_pedido: Um identificador único para o pedido.
        ◦ Adicione métodos para:
            ▪ Adicionar pizzas ao pedido.
            ▪ Calcular o total do pedido.
            ▪ Exibir os detalhes do pedido.
```
