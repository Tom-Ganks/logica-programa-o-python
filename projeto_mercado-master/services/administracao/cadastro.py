from database.connection import conn

TABLE_NAME = 'produto'

def cadastro():
    nome = input('Digite o nome do produto: ')
    quant = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço: '))

    connection = conn()

    with connection:
        with connection.cursor() as cursor:
            cursor.execute( 
                f'''
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    codigo INT NOT NULL AUTO_INCREMENT, 
                    nome VARCHAR(50) NOT NULL, 
                    quantidade INT NOT NULL, 
                    preco DECIMAL(10, 2) NOT NULL, 
                    PRIMARY KEY (codigo)
                )
                '''
            )

        sql = f'INSERT INTO {TABLE_NAME} (nome, quantidade, preco) VALUES (%s, %s, %s)'
        data = (nome, quant, preco)
        
        with connection.cursor() as cursor:
            rows_affected = cursor.execute(sql, data)
            print(f"Produto inserido: {nome}, Quantidade: {quant}, Preço: {preco}")
            print(f"Linhas afetadas: {rows_affected}")
        
        connection.commit()

