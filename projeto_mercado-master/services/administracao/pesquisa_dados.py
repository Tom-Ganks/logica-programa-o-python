from database.connection import conn
from models.cliente import Cliente
from models.funcionario import Funcionario

def pesquisa_cliente():
    TABLE_NAME = 'cliente'
    print('####### Pesquisa de cliente ########')
    cpf = input('Digite o cpf do cliente: ')
    connection = conn()

    sql = f'SELECT * FROM {TABLE_NAME} c JOIN pessoa p ON p.id = c.idpessoa WHERE p.cpf = {cpf};'
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            dados = cursor.fetchone()
    
    if dados:
        cliente = Cliente(
            nome=dados['nome'], 
            sexo=dados['sexo'], 
            cpf=dados['cpf'],
            telefone=dados['telefone'],
            email=dados['email']
        )
        cliente.endereco = dados['endereco']
        return cliente
    else:
        return None
    
def pesquisa_funcionario():
    TABLE_NAME = 'funcionario'
    connection = conn()

    print('####### Pesquisa de funcionário ########')
    matricula = input('Digite a matricula do funcionário: ')
    sql = f'SELECT * FROM {TABLE_NAME} f JOIN pessoa p ON p.id = f.idpessoa WHERE f.matricula = {matricula};'
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            funcionario = cursor.fetchone()
    
    if funcionario:
        funcionario = Funcionario(
            nome=funcionario['nome'], 
            sexo=funcionario['sexo'], 
            cpf=funcionario['cpf'],
            telefone=funcionario['telefone'],
            email=funcionario['email'],
            matricula=funcionario['matricula'],
            funcao=funcionario['funcao'],
            salario=funcionario['salario']
        )
        return funcionario
    else:
        return None