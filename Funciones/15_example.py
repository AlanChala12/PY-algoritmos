# Construir una función que reciba como parámetro dos enteros y retorne 1 si la diferencia entre los dos valores es un número primo. Deberá retornar 0 si no es así.
def diferencia_prima(n1, n2):
  diferencia = abs(n1 - n2)
  es_primo = True

  for i in range(2, diferencia):
    if diferencia % i == 0:
      es_primo = False
      break

  if es_primo == True and diferencia > 1:
    return 1
  else:
    return 0

entero1 = int(input('Ingresa un número entero: '))
entero2 = int(input('Ingresa otro número entero: '))
print(diferencia_prima(entero1, entero2))