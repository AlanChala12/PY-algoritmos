# Leer 10 números enteros, almacenarlos en un vector. Luego leer un entero y determinar si este último entero se encuentra entre los 10 valores almacenados en el vector

try:
  numeros = [int(input(f'Entero {i + 1}: ')) for i in range(10)]
  entero = int(input('Ingresa un número entero: '))

  if entero in numeros:
    print(f'El número {entero} SE ENCUENTRA en el vector {numeros}')
  else:
    print(f'El número {entero} NO SE ENCUENTRA en el vector {numeros}')

except ValueError:
  print('Por favor, ingresa valores numéricos')