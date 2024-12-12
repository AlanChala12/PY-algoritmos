# Leer tres números enteros y determinar si el último dígito de los tres números es igual 
entero_uno = int(input('Ingresa un número entero: '))
entero_dos = int(input('Ingresa un número entero más: '))
entero_tres = int(input('Ingresa otro número entero: '))

last_dig_uno = entero_uno % 10
last_dig_dos = entero_dos % 10
last_dig_tres = entero_tres % 10

if last_dig_uno == last_dig_dos and last_dig_uno == last_dig_tres:
  print(f'Los últimos dígitos de los números {entero_uno}, {entero_dos}, y {entero_tres} son iguales.')

else:
  print(f'Los últimos dígitos de los números {entero_uno}, {entero_dos}, y {entero_tres} no son iguales.')