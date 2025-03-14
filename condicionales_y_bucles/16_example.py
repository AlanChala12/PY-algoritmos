# Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos
x = int(input('Primer entero: '))
y = int(input('Segundo entero: '))

digitos_x = 0
digitos_y = 0

while x != 0:
  digitos_x += 1
  x //= 10

while y != 0:
  digitos_y += 1
  y //= 10

if digitos_x > digitos_y:
  print(f'El primer número, tiene más dígitos que el segundo.')

elif digitos_y > digitos_x:
  print(f'El segundo número, tiene más dígitos que el primero.')

else:
  print('--Ambos números tienen la misma cantidad de dígitos--')