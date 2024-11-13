# Leer un número entero de dos dígitos y determinar sisus dos dígitos son primos.


number = int(input('Ingresa un número mayor o igual a 10: '))

"""Se obtiene el primer dígito."""
dig1 = int(number / 10)

"""Se obtiene el segundo dígito"""
dig2 = int(number / 10) * 10
dig2 = number - dig2

if number >= 10:

  #Verificar si el primer dígito es primo.
  x1 = dig1 / dig1
  xx1 = dig1 / 1

  #Verificar si el segundo dígito es primo.
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
