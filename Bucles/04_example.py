"""Hallar la cantidad de dígitos de un número que ingresa por teclado."""

number = int(input('Entero: '))
cantidad_digitos = 0

while number != 0:
  
  cantidad_digitos += 1
  number //= 10
  
print(f'La cantidad de dígitos del número proporcionado es de {cantidad_digitos}')