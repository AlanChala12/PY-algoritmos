# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentra el número mayor.
numeros = [ int(input(f'Entero { i + 1 }: ')) for i in range(10) ]
max_num = max( numeros )

print(f'El número mayor "{max_num}" se encuentra en el indice {numeros.index(max_num)}')