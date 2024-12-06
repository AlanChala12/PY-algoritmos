# Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo
number = int(input('Numero: '))

if number < 1000:
  print(f'Ingresa un valos númerico mayor o igual a mil')

else:
  dig2 = (number // 100) % 10
  dig3 = (number // 10) % 10

  if dig2 == dig3:
    print(f'El segundo dígito del número {number} es igual al penúltimo.')

  else:
    print(f'El segundo dígito del número {number} no es igual al penúltimo.')