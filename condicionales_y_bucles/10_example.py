# Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.
contador = 0

for x in range(1, 60 + 1):
    
    if x % 3 == 0:
        contador = contador + x

print(f'La suma de los primeros veinte múltiplos de tres, es de: {contador}')