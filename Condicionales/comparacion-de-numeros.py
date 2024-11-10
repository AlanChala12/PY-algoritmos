print("---Verificación de igualdad de dos números---")
print()
number1 = int(input('Ingresa un número entero: '))
number2 = int(input('Ingresa otro número entero: '))

if number1 > number2: 
  print(f'{number1} es mayor que {number2}.')
elif number2 > number1:
  print(f'{number2} es mayor que {number1}.')
else:
  print('Ambos números son iguales.')