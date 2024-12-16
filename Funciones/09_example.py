# Construir una función que reciba como parámetros dos números enteros y retorne 1 si el primer número es múltiplo del segundo y 0 si no.
def multiplo(n1, n2):

  if n1 <= 0 or n2 <= 0:
    return '--Ingresa un número positivo o diferente de cero--'

  else:
    if n1 % n2 == 0:
      return 1
    else:
      return 0
  
entero_uno = int(input('Ingresa un número entero:'))
entero_dos = int(input('Ingresa otro número entero: '))
print(multiplo(entero_uno, entero_dos))