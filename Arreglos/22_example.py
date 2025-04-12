# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el número con más dígitos.

enteros = [ int(input(f'Entero { i + 1 }: ')) for i in range( 10 ) ]
maxNum = max( enteros )

print(f'Número con más dígitos: { maxNum } - Posición: { enteros.index( maxNum ) + 1 }')