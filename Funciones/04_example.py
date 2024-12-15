# Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si dicho entero es múltiplo de dicho dígito y 0 si no es así.

entero = int(input('Ingresa un número entero: '))
digito = int(input('Ingresa un dígito[0,...,9]: '))

def verificacion(x, n):
  if x == 0:
    return 'Ingresa un valor distinto de cero'
  elif n % x == 0:
    return 1
  else:
    return 0

result = verificacion(entero, digito)
print(result)