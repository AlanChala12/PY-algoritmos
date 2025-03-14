# Leer un número entero y determinar a cuánto es igual la suma de sus dígitos pares.
number = int(input('Entero: '))
digitos_pares = 0
suma_de_digitos = 0

while number != 0:
  digitos_pares = number % 10
  
  if digitos_pares % 2 == 0:
    suma_de_digitos = suma_de_digitos + digitos_pares

  number //= 10

print(f'La suma de dígitos pares del número proporcionado es de {suma_de_digitos}.')