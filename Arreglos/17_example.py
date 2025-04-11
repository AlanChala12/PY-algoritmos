# Leer 10 números enteros, almacenarlos en un vector y determinar cuál es el número menor.

enteros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
minNum = min( enteros )
print( f'Número menor: { minNum }' )