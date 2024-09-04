from models.produto import Produto
from utils import impressao

from database.connection import conn
from utils.impressao import impressao

TABLE_NAME = 'produto'

def lista_produtos():
    connection = conn()

    sql = f'SELECT * FROM {TABLE_NAME} LIMIT 100;'
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            produtos = cursor.fetchall()

    print('\n##### Lista de Produtos #####')
    
    for produto in produtos:
        produto = Produto(
            codigo=produto['codigo'], 
            nome=produto['nome'], 
            quantidade=produto['quantidade'], 
            preco=produto['preco']
        )
        impressao(produto)
        print('')
