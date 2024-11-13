# Leer un número entero y mostrar en pantalla su tabla de multiplicar.

try:

  number = int(input('¿Qué tabla quieres ver?'))
  print(f'---Tabla del {number}---')

  for table in range(1, 11, 1):

    result = number * table
    print(f'{number} x {table} = {result}')

except:

  print('!ERROR¡ ingresa un valor númerico.')