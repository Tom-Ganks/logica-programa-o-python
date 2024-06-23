def contar_numbers_positivos():
    contador = 0
    
    while True:
        number = float(input("Digite um número (digite um número negativo para parar): "))
        
        if number < 0:
            break
        
        contador += 1
    
    print(f"Foram digitados {contador} números positivos")

#Não esqueça do chamado para iniciar a função def
contar_numbers_positivos()