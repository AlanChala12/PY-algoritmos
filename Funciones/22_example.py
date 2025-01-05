# Construir una función que reciba como parámetro un entero y retorne 1 si en dicho valor el primer dígito es igual al último. Deberá retornar 0 si no es así.
def comparacion_de_digitos(n):

  entero = str(n)
  if entero[-1] == entero[0]:
    return 1
  else: 
    return 0

try:
  entero = int(input('Ingresa un número entero: '))
  print(comparacion_de_digitos(entero))
except ValueError:
  print('Por favor ingresa un valor númerico')