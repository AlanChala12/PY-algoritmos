# Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.
x = int(input('Ingresa un entero positivo: '))
print(f'Los divisores del número {x}, son:')

for y in range(1, x, 1):
    
    if x % y == 0:
        print(y)
    else:
        continue