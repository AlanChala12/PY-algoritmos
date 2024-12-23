# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentran los números con más de 3 dígitos.

numeros = []
for i in range(0, 11):
    numero = int(input(f'Entero {i}: '))
    numeros.append(numero)
    
for x in numeros:
    if x >= 100:
        print(f'El número {x} se encuentra en el indice {numeros.index(x)}')

print()
print(numeros)