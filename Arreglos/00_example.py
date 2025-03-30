# Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número leído.

try:
  enteros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
  numero_mayor = max(enteros)
  print(f'El número mayor { numero_mayor }, del vector {enteros}, se encuentra en la posición: { enteros.index(numero_mayor) }')
  
except ValueError:
  print('Por favor, ingresa números enteros')
