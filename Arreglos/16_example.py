# Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números negativos hay.

enteros = [ int(input(f'Entero { i + 1 }: ')) for i in range( 10 ) ]
negativos = 0

for x in enteros:
  if x < 0:
    negativos += 1
    
if negativos != 0:
  print(f'Hay { negativos } números negativos en el vector { enteros }')
  
else:
  print(f'No se encuentran números negativos en el vector { enteros }')