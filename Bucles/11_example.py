# Leer un número entero y determinar a cuánto es igual el promedio entero de sus dígitos.

number = int(input('Entero: '))
cantidad_de_digitos = 0
suma_de_digitos = 0

while number != 0:

  suma_de_digitos = suma_de_digitos + (number % 10)
  cantidad_de_digitos += 1
  number //= 10

promedio = suma_de_digitos // cantidad_de_digitos

print(f'El promedio entero de los dígitos del número proporcionado es de {promedio}')