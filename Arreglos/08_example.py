# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentra el número mayor.
numeros = []

for i in range(0, 11):
    numero = int(input(f'Entero {i}: '))
    numeros.append(numero)
    
max_num = max(numeros)
print(f'El número mayor "{max_num}" se encuentra en el indice {numeros.index(max_num)}')