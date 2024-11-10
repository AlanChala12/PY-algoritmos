number = int(input("Ingresa un número entero de dos dígitos: "))

dig1 = int(number / 10)

dig2 = int(number / 10) * 10
dig2 = number - dig2

if dig1 == dig2:
  print(f'Los dígitos que conforman al número {number}, son iguales.')
else: 
  print(f'Los dígitos que conforman al número {number}, no son iguales.')