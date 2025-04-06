# Leer 10 números enteros, almacenarlos en un vector y determinar si el promedio entero de estos datos está almacenado en el vector.

numeros = [ int(input(f'Entero {i + 1}: ')) for i in range( 10 ) ]
promedio = max( numeros ) // len( numeros )

if promedio in numeros:
    print(f'El promedio entero { promedio } se encuentra en el vector { numeros }')
else:
    print(f'El promedio entero { promedio } NO SE encuentra en el vector { numeros }')