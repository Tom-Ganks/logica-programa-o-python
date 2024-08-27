from services.pizzaria import pizzaria

def main():
    numero_pedido = 1
    while True:
        print('')
        opcao = int(input('1- Novo Pedido\n'
            '2- Sair\n'
            'Escolha a opção desejada: '
    ))  
        
        if opcao == 1:
            pizzaria(numero_pedido)
            numero_pedido += 1
        else:
            break

if __name__ == '__main__':
    main()