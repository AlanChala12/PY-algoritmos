# Leer un número entero y determinar si tiene 3 dígitos.
number = 2

if number >= 0 and number < 10:
  print('Es un número de 1 dígito.')

elif number >= 10 and number < 100:
  print('Es un número de 2 dígitos.')

elif number >= 100 and number < 1000:
  print('Es un número de 3 dígitos.')

else:
  print('El número tiene 4 dígitos o más.')