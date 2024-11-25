# Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.
number1 = int(input('Ingresa un número entero: '))
number2 = int(input('Ingresa un número entero más: '))
number3 = int(input('Ingresa otro más: '))

dig1_number1 = number1 // 10
dig2_number1 = number1 % 10

dig1_number2 = number2 // 10
dig2_number2 = number2 % 10

dig1_number3 = number3 // 10
dig2_number3 = number3 % 10

dig_max_number1 = max(dig1_number1, dig2_number1)
dig_max_number2 = max(dig1_number2, dig2_number2)
dig_max_number3 = max(dig1_number3, dig2_number3)

result = max(dig_max_number1, dig_max_number2, dig_max_number3)

if dig_max_number1 > dig_max_number2 and dig_max_number1 > dig_max_number3:
  print(f'El dígito mayor, se encuentra en el número {number1}')

elif dig_max_number2 > dig_max_number1 and dig_max_number2 > dig_max_number3:
  print(f'El dígito mayor, se encuentra en el número {number2}')

elif dig_max_number3 > dig_max_number1 and dig_max_number3 > dig_max_number2:
  print(f'El dígito mayor, se encuentra en el número {number3}')

else:
  print(f'El dígito mayor se encuentra en varios números proporcionados')