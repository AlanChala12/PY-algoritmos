# Leer un número entero y determinar si es múltiplo de 7.
entero = int(input('Entero: '))

if entero % 7 == 0:
  print(f'El número {entero} es múltiplo de 7.')
else:
  print(f'El número {entero} no es múltiplo de 7.')