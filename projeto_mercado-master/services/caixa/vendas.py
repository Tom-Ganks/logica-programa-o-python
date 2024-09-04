from database.connection import conn
from models.produto import Produto
from utils.impressao import impressao

TABLE_NAME = 'produto'

def venda_produto():
    print('###### Venda de Produto ########')
    codigo = input('Digite o código do produto: ')

    sql = f'SELECT * FROM {TABLE_NAME} WHERE codigo = {codigo};'
    connection = conn()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            produto = cursor.fetchone()

        perc = None
        quant = 0
        
        valor_desconto = 0.0
        
        if produto:
            produto = Produto(
                codigo=produto['codigo'], 
                nome=produto['nome'], 
                quantidade=produto['quantidade'], 
                preco=float(produto['preco'])
            )
            
            quant = int(input('Digite a quantidade: '))
            if quant > produto.quantidade:
                print(f'Estoque insuficiente: {produto.quantidade}')
            else:
                produto.quantidade -= quant
                perc = float(input('Digite o percentual do desconto: '))
                valor_desconto = produto.desconto(perc)
                
                impressao(produto)
                print(f'Preço com desconto: {valor_desconto}')
                print(f'Total: {valor_desconto * quant}')  
                print('')
                # Atualizo o estoque
                sql = f'UPDATE {TABLE_NAME} SET quantidade = quantidade - {quant} WHERE codigo = {codigo};'
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                connection.commit()
        else:
            print('Produto não encontrado!')
            print('')
        
        