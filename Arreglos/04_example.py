# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentran los números terminados en 4.

enteros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
print('---Terminados en cuatro---')

for x in enteros:
  if x % 10 == 4:
    print( f'Número: {x}, Indice: { enteros.index(x) + 1 }' )