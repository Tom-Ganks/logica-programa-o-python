<<<<<<< HEAD
def contar_numbers_positivos():
    contador = 0
    
    while True:
        number = float(input("Digite um número (digite um número negativo para parar): "))
        
        if number < 0:
            break
        
        contador += 1
    
    print(f"Foram digitados {contador} números positivos")

#Não esqueça do chamado para iniciar a função def
=======
def contar_numbers_positivos():
    contador = 0
    
    while True:
        number = float(input("Digite um número (digite um número negativo para parar): "))
        
        if number < 0:
            break
        
        contador += 1
    
    print(f"Foram digitados {contador} números positivos")

#Não esqueça do chamado para iniciar a função def
>>>>>>> 275cba4d39bb3b4df361b0ad2021c2b179d3c4da
contar_numbers_positivos()