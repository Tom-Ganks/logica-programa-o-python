from database.connection import conn

def cadastro_pessoa(op):
    connection = conn()

    with connection:
        nome = input('Digite o nome: ')
        sexo = input('Digite o sexo: ')
        cpf = input('Digite o CPF: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')

        # Criar a tabela pessoa
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS pessoa (
                    id INT NOT NULL AUTO_INCREMENT,
                    nome VARCHAR(150) NOT NULL,
                    sexo CHAR(1) NOT NULL,
                    cpf VARCHAR(11) NOT NULL,
                    telefone VARCHAR(11) NOT NULL,
                    email VARCHAR(150),
                    PRIMARY KEY (id)
                )
                '''
            )

        # Inserir dados na tabela pessoa e obter o ID gerado
        sql_pessoa = 'INSERT INTO pessoa (nome, sexo, cpf, telefone, email) VALUES (%s, %s, %s, %s, %s)'
        data_pessoa = (nome, sexo, cpf, telefone, email)

        with connection.cursor() as cursor:
            cursor.execute(sql_pessoa, data_pessoa)
            idpessoa = cursor.lastrowid  # Obtém o último ID inserido

        if op == 1:
            # Cadastro de cliente
            endereco = input('Digite o endereço: ')

            # Criar a tabela cliente
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    CREATE TABLE IF NOT EXISTS cliente (
                        idcliente INT NOT NULL AUTO_INCREMENT,
                        idpessoa INT NOT NULL,
                        ativo bool default true,
                        endereco VARCHAR(100) NOT NULL,
                        FOREIGN KEY(idpessoa) REFERENCES pessoa(id),
                        PRIMARY KEY (idcliente)
                    )
                    '''
                )

            # Inserir dados na tabela cliente
            sql_cliente = 'INSERT INTO cliente (idpessoa, endereco) VALUES (%s, %s)'
            data_cliente = (idpessoa, endereco)
            
            with connection.cursor() as cursor:
                cursor.execute(sql_cliente, data_cliente)

            print(f"Cliente inserido: {nome}, sexo: {sexo}, cpf: {cpf}")

        elif op == 2:
            # Cadastro de funcionário
            matricula = input('Digite a matrícula: ')
            funcao = input('Digite a função: ')
            salario = float(input('Digite o salário: '))

            # Criar a tabela funcionário
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    CREATE TABLE IF NOT EXISTS funcionario (
                        idfunc INT NOT NULL AUTO_INCREMENT,
                        idpessoa INT NOT NULL,
                        matricula VARCHAR(100) NOT NULL,
                        funcao VARCHAR(50) NOT NULL,
                        salario DECIMAL(10, 2) NOT NULL,
                        FOREIGN KEY(idpessoa) REFERENCES pessoa(id),
                        PRIMARY KEY (idfunc)
                    )
                    '''
                )

            # Inserir dados na tabela funcionário
            sql_funcionario = 'INSERT INTO funcionario (idpessoa, matricula, funcao, salario) VALUES (%s, %s, %s, %s)'
            data_funcionario = (idpessoa, matricula, funcao, salario)
            
            with connection.cursor() as cursor:
                cursor.execute(sql_funcionario, data_funcionario)

            print(f"Funcionário inserido: {nome}, sexo: {sexo}, cpf: {cpf}")

        connection.commit()
