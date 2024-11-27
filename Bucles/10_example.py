# Leer un número entero y determinar a cuánto es igual la suma de sus dígitos.

number = int(input('Entero: '))
suma_digitos = 0

while number != 0:
  suma_digitos = suma_digitos + (number % 10)
  number //= 10

print(f'La suma de de los dígitos del número proporcionado es de {suma_digitos}')