# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones están los números positivos.
enteros = []
positivos = []

for i in range(1, 11):
  numeros = int(input(f'Entero {i}: '))
  enteros.append(numeros)

print()
print('Valor / Indice')

for indice, valor in enumerate(enteros):
  if valor > 0:
    print(f'{valor}: {indice}')

if len(positivos) == 0:
  print(f'No hay números negativos en el vector {enteros}')