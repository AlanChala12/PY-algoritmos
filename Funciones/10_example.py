# Construir una función que reciba como parámetro un entero y retorne 1 si dicho valor es un número de mínimo 3 dígitos. Deberá retornar 0 si no es así.
def cantidad_de_digitos(number):
  if number >= 100:
    return 1
  else:
    return 0

entero = int(input('Ingresa un número: '))
print(cantidad_de_digitos(entero))