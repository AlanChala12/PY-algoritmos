# Leer dos números enteros y determinar cuál es múltiplo de cuál.
entero_uno = int(input('Ingresa un número: '))
entero_dos = int(input('Ingresa otro número: '))

if entero_uno % entero_dos == 0:
  print(f'{entero_dos} es múltiplo de {entero_uno}.')

elif entero_dos % entero_uno == 0:
  print(f'{entero_uno} es múltiplo de {entero_dos}.')

else:
  print(f'Ningún número de los proporcionados es múltiplo del otro número proporcionado')