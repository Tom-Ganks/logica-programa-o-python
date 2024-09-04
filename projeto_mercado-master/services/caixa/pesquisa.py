from models.produto import Produto
from utils.impressao import impressao

from database.connection import conn


TABLE_NAME = 'produto'

def pesquisa():
    print('####### Pesquisa de Produto ########')
    codigo = input('Digite o código do produto que deseja buscar: ')
   
    connection = conn()

    sql = f'SELECT * FROM {TABLE_NAME} WHERE codigo = {codigo};'
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            produto = cursor.fetchone()
    
    if produto:
        produto = Produto(
            codigo=produto['codigo'], 
            nome=produto['nome'], 
            quantidade=produto['quantidade'], 
            preco=produto['preco']
        )
        impressao(produto)
        print('')
    else:
        print('Produto não encontrado!')
        print('')