# Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número leído.
enteros = []
for i in range(0, 10):
  numero = int(input('Entero: '))
  enteros.append(numero)

numero_mayor = max(enteros)
posicion = enteros.index(numero_mayor)

print(f'El número {numero_mayor} se encuentra en la posición {posicion}')
print(enteros)