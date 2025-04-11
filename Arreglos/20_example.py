# Leer 10 números enteros, almacenarlos en un vector y determinar si el promedio entero de dichos números es un número primo.

enteros = [ int(input(f'Entero {i + 1}: ')) for i in range( 10 ) ]
promedio = sum( enteros ) // len( enteros )
esPrimo = True

for i in range( 2, promedio ):
  if promedio % i == 0:
    esPrimo = False
    break
  
if esPrimo:
  print(f'El promedio entero del vector { enteros }, ES un número primo')
else:
  print(f'El promedio entero { promedio } del vector { enteros }, NO ES un número primo')
  