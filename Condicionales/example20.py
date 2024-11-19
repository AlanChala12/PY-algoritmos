# Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
try:
  number = int(input('Ingresa un número entero positivo de tres dígitos: '))

  if number >= 100 and number < 1000:
      xx = number // 10
      dig1 = xx // 10
      dig2 = xx % 10
      dig3 = number % 10

      if dig1 > dig2 and dig1 > dig3:
        print(f'El dígito mayor del número {number}, se encuentra en la posición "UNO".')

      elif dig2 > dig1 and dig2 > dig3:
        print(f'El dígito mayor del número {number}, se encuentra en la posición "DOS".')

      elif dig3 > dig1 and dig3 > dig2:
        print(f'El dígito mayor del número {number}, se encuentra en la posición "TRES".')

      else:
        print(f'Los dígitos que conforman al número {number}, son IGUALES.')
  
  else:
    print('---El número proporcionado es demasiado pequeño---')

except:
  print('!ERROR¡ formato invalido')