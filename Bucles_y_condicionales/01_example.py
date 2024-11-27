# Leer dos números enteros y determinar cuál de los dos tiene más dígitos.

number_one = int(input('Entero: '))
number_two = int(input('Otro Entero: '))

digitos_number_one = 0
digitos_number_two = 0

"""Cantidad de dígitos del número uno."""
while number_one != 0:

  number_one = number_one // 10
  digitos_number_one = digitos_number_one + 1

"""Cantidad de dígitos del número dos."""
while number_two != 0:

  number_two = number_two // 10
  digitos_number_two = digitos_number_two + 1


if digitos_number_one > digitos_number_two:
  print('El primero número tiene mas dígitos que el segundo número.')
  
elif digitos_number_two > digitos_number_one:
  print('El segundo número tiene mas dígitos que el primer número.')
  
else:
  print('Ambos tienen la misma cantidad de dígitos.')


