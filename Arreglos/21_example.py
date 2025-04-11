# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones están los números positivos.

enteros = [ int(input(f'Entero {i + 1}: ')) for i in range( 10 ) ]
positivos = 0

print('##Números positivos##')

for i, n in enumerate( enteros ):
  
  if n > 0:
    positivos += 1
    print(f'Número: { n } - Posición: { i + 1 }')
    
if positivos == 0:
  print(f'No se encontraron números positivos en el vector { enteros }')

