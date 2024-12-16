# Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si dicho dígito está en dicho entero y 0 si no es así.
def verificacion(n, d):
  entero = str(n)
  digito = str(d)

  if digito in entero:
    return 1
  else:
    return 0

number = int(input('Ingresa un número entero: '))
dig = int(input('Ingresa un dígito [0,..,9]: '))
result = verificacion(number, dig)
print(result)