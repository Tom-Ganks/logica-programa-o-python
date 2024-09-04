from database.connection import conn
from models.produto import Produto
from utils.impressao import impressao

TABLE_NAME = 'produto'

def reajuste_produto():
    print('###### Reajuste de Produto ########')
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
    
                perc = float(input('Digite o percentual do aumento: '))
                preco_reajustado = produto.reajuste(perc)
                produto.preco = preco_reajustado
            
                # Atualizo o preço
                sql = f'UPDATE {TABLE_NAME} SET preco = {produto.preco} WHERE codigo = {codigo};'
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                connection.commit()   
                impressao(produto)
            else:
                print('Produto não encontrado!')