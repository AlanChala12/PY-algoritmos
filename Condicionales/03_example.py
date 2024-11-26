# Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
number = int(input("Entero: "))

dig1 = number // 10
dig2 = number % 10

if number < 10:
  print(f'--El número debe ser mayor o igual a diez--')

elif dig1 == dig2:
  print(f'Los dígitos que conforman al número {number}, son iguales.')
  
else: 
  print(f'Los dígitos que conforman al número {number}, no son iguales.')