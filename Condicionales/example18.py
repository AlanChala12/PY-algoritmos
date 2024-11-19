# Leer tres números enteros y mostrarlos ascendentemente.

number1 = int(input('ingresa un número entero: '))
number2 = int(input('ingresa otro número entero: '))
number3 = int(input('ingresa un número entero más: '))

if number1 > number2 and number1 > number3 and number2 > number3:
  print(f'{number1}, {number2}, {number3}')

elif number1 > number2 and number1 > number3 and number3 > number2:
  print(f'{number1}, {number3}, {number2}')

elif number2 > number1 and number2 > number3 and number1 > number3:
  print(f'{number2}, {number1}, {number3}')

elif number2 > number1 and number2 > number3 and number3 > number2:
  print(f'{number2}, {number3}, {number1}')

elif number3 > number1 and number3 > number2 and number1 > number2:
  print(f'{number3}, {number1}, {number2}')

elif number3 > number1 and number3 > number2 and number2 > number1:
  print(f'{number3}, {number2}, {number1}')

else:
  print('---Los números proporcionados son iguales---')