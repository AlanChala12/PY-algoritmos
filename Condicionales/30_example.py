# Leer un número entero de tres dígitos y determinar si alguno de sus dígitos es igual a la suma de los otros dos.
entero = int(input('Entero: '))

if entero < 100 or entero > 999:
    print('Por favor, ingresa un número de tres dígitos.')

else:
  dig1 = entero // 100
  dig2 = (entero // 10) % 10
  dig3 = entero % 10

  if dig1 + dig2 == dig3:
    print(f'La suma de los dígitos {dig1} y {dig2} da como resultado el dígito {dig3}.')

  elif dig1 + dig3 == dig2:
    print(f'La suma de los dígitos {dig1} y {dig3} da como resultado el dígito {dig2}.')
  
  elif dig3 + dig2 == dig1:
    print(f'La suma de los dígitos {dig2} y {dig3} da como resultado el dígito {dig1}.')

  else:
    print(f'--Ninguno de los dígitos es igual a la suma de los otros dos--')