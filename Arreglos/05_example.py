# Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces está repetido el mayor.

try:
  enteros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
  apariciones = 0
  numero_mayor = max( enteros )

  for x in enteros:
    if x == numero_mayor:
      apariciones += 1
      
  print(f'El número mayor {numero_mayor}, del vector { enteros }, se encuentra { apariciones } vez/veces')
  
except ValueError:
  print('Por favor, ingresa valores numéricos')