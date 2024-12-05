# Leer un número entero menor que 1000 y determinar cuántos dígitos tiene.
number = int(input('Entero: '))

if number < 10:
  print(f'El número {number} tiene solo un dígito.')

elif number < 100:
  print(f'El número {number} tiene dos dígitos.')

elif number < 1000:
  print(f'El número {number} tiene tres dígitos.')

else:
  print(f'El número {number} tiene cuatro o más dígitos.')