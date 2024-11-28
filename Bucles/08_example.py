# Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.
x = int(input('Entero: '))
cantidad = 0

for i in range(1, x + 1):
    cantidad = cantidad + i

print(f'La suma es de: {cantidad}.')