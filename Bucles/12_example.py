# Leer un número entero y determinar cuál es el mayor de sus dígitos.

number = int(input('Entero: '))
ultimo_digito = 0
digitos = []

while number != 0:
  ultimo_digito = number % 10
  digitos.append(ultimo_digito)
  number //= 10

numero_mayor = max(digitos)
print(f'El mayor de los dígitos del número proporcionado es {numero_mayor}')