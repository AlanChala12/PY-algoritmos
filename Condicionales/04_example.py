# Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos.
number = int(input('Ingresa un número mayor o igual a 10: '))

dig1 = number // 10
dig2 = number % 10

if number >= 10:

  x1 = dig1 / dig1
  xx1 = dig1 / 1

  y2 = dig2 / dig2
  yy2 = dig2 / 1

  if x1 == 1 and xx1 == dig1 and y2 == 1 and yy2 == dig2:
    print(f'Ambos dígitos que conforman el número {number}, son primos')
    
  elif x1 == 1 and xx1 == dig1 or y2 == 1 and yy2 == dig2:
    print(f'Solo un dígito del número {number}, es primo.')
    
  else:
    print(f'Ningún dígito del número {number}, es primo.')

else:
  print(f'El número {number}, debe ser mayor o igual a 10.')
