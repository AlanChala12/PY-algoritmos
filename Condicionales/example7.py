# Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.


x = int(input('Ingresa un número: '))

if x >= 1:

  xx = x / x
  yy = x / 1

  if xx == 1 and yy == x:
    print(f'El número {x}, es primo.')
  else:
    print(f'El número {x}, no es primo.')

else:
  print(f'El número {x}, no es primo ya que no cumple la primera condición de los números primos "n > 1"')