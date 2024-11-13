# Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.


user_name = int(input('Ingresa un número entero positivo de dos dígitos: '))

if user_name < 10:
  user_name += 10

elif user_name > 10:
  dig1 = int(user_name / 10)

  dig2 = int(user_name / 10) * 10
  dig2 = user_name - dig2

  if dig1 % 2 == 0 and dig2 % 2 == 0:
    print(f'Ambos dígitos del número {user_name}, son pares.')
    
  else:
    print(f'Solo uno o ningúno de los dígitos del número {user_name}, son pares.')