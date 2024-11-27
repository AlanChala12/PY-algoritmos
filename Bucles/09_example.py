#Leer un número entero y determinar cuántos dígitos tiene.

number = int(input('Entero: '))
x = number
cantidad_digitos = 0

while x != 0:

  x //= 10
  cantidad_digitos += 1

print(f'La cantida de dígitos del número {number} es {cantidad_digitos}')