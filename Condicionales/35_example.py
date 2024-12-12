# Leer un número entero de dos dígitos, guardar cada dígito en una variable diferente y luego mostrarlas en pantalla.
entero = int(input('Entero: '))

if entero < 10 or entero > 100:
  print(f'Proporciona un número que contenga dos dígitos.')

else:
  dig1 = entero // 10
  dig2 = entero % 10
  print(f'{dig1} y {dig2}')