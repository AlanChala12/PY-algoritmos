# Leer 10 números enteros, almacenarlos en un vector y determinar si la semisuma entre el valor mayor y el valor menor es un número par.

try: 
    numeros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]

    valor_max = max(numeros)
    valor_min = min(numeros)
    
    if valor_min == 0 or valor_max == 0:
        print('¡ERROR! no se puede dividir entre cero')
    else:
        semisuma = valor_max / valor_min
        
        if semisuma % 2 == 0:
            print(f'La semisuma entre {valor_max} y {valor_min} ES un número par!')
        
        else:
            print(f'La semisuma entre {valor_max} y {valor_min} NO ES número par!')
            
except ValueError:
    print('Por favor, ingresa valores numéricos')