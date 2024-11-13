# Mostrar en pantalla la tabla de multiplicar del número 5.

x = 5
print(f'---Tabla del {x}---')

for dig in range(1, 11, 1):

  xx = x * dig
  print(f'{x} x {dig} = {x}')