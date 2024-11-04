"""Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído."""

number = int(input('Ingresa un número entero positivo: '))

while number > 1:
  number -= 1

  if number % 2 == 0:
    print(number)
  else:
    print()

