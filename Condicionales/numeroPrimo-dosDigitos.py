number = int(input('Ingresa un número entero de dos dígitos, menor que 20: '))

if number > 20:
  print('El número debe ser menor que 20 y mayor o igual a 10.')

elif number <= 20 and number >= 10:

  division = number / number
  division_por_uno = number / 1

  if division == 1 and division_por_uno == number:
    print(f'El número {number}, es primo.')
  else:
    print(f'El número {number}, no es primo.')

else:
  print('El número debe estar entre 10 y 20.')