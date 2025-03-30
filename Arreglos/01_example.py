# Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número par leído.

enteros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
pares = [ x for x in enteros if x % 2 == 0 ]
par_mayor = max( pares )

print(f'El mayor número par { par_mayor }, del vector {enteros}, se encuentra en la pocisión: { enteros.index( par_mayor ) + 1 }')