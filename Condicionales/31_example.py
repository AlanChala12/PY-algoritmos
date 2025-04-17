# Leer un número entero de cuatro dígitos y determinar a cuánto es igual la suma de sus dígitos.

num = int(input('Entero: '))

if 1000 <= num < 10000:
  sumNum = 0
  for i in str(num):
    sumNum = sumNum + int(i)
  print(f'Suma de dígitos del número { num }, es: { sumNum }')
  
else:
  print('Ingresa un número que contenga cuatro dígitos')

