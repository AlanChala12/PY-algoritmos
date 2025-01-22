# Leer 10 números enteros, almacenar los en un vector y determinar cuántos números de los almacenados en dicho vector terminan en 5.

try: 
    numeros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
    terminados_en_cinco = [ x for x in numeros if x % 10 == 5 ]
    print(f'La cantidad de números terminados en 5, son: {len(terminados_en_cinco)}')
    
except ValueError:
    print('Por favor, ingresa valores numéricos')