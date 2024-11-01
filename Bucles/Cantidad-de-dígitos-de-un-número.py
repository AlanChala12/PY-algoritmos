"""Hallar la cantidad de dígitos de un número que ingresa por teclado."""

x = int(input('Ingresa un número: '))
cd = 0

while x != 0:
  x = int(x / 10)
  cd = cd + 1

print(cd)