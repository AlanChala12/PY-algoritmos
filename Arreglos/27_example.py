# Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual la suma de los dígitos pares de cada uno de los números leídos.

try: 
    numeros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
    pares = [ x for x in numeros if x % 2 == 0 ]

    sum_pares = sum(pares)
    print(f'La suma de los números pares del vector {numeros}, es de: {sum_pares}')
    
except ValueError:
    print('Por favor, ingresa valores numéricos')
    