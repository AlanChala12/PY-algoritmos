# Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual el promedio entero de los datos del vector.

numeros = [ int(input(f'Entero { i + 1 }: ')) for i in range( 10 ) ]
promedio = sum( numeros ) // len( numeros )

print(f'El promedio entero del vector { numeros }, es: { promedio }')