# Leer un número entero de cuatro dígitos y determinar a cuánto es igual la suma de sus dígitos.
entero = int(input('Entero: '))

if entero < 1000 or entero > 10000:
  print('Por favor, ingresa un número que contenga cuatro dígitos.')

else:
  dig1 = entero // 1000
  dig2 = (entero // 100) % 10
  dig3 = (entero // 10) % 10
  dig4 = entero % 10

  result = dig1 + dig2 + dig3 + dig4
  print(f'La suma de los dígitos del número {entero}, es igual a {result}')