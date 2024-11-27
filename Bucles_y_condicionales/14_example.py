# Leer un número entero y determinar cuántas veces tiene el dígito 1.
 
number = int(input('Entero: '))
number = str(number)
cantidad_de_unos = 0

for x in number:

  if "1" in x:
    cantidad_de_unos += 1

print(f'El número {number} tiene {cantidad_de_unos} veces el número "uno"')