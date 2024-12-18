# Construir una función que reciba como parámetro dos enteros de dos dígitos cada uno y retorne 1 si son inversos. Ejemplo: 83 es inverso de 38. Deberá retornar 0 si no es así.
def es_inverso(a, b):

  entero_uno = str(a)
  entero_dos = str(b)

  if len(entero_uno) == 2 and len(entero_dos) == 2:
    entero_uno_invertido = entero_uno[::-1]

    if entero_uno_invertido == entero_dos:
      return 1
    else:
      return 0

  else:
    return 'Ambos números deben ser de dos dígitos'

numero_uno = int(input('Ingresa un número entero: '))
numero_dos = int(input('Ingresa otro número entero: '))
print(es_inverso(numero_uno, numero_dos))