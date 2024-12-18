# Construir una función que reciba como parámetro un entero y retorne 1 si dicho valor es múltiplo de 5. Deberá retornar 0 si no es así.
def multiplo_de_cinco(entero):

  if entero % 5 == 0:
    return 1
  else:
    return 0

number = int(input('Ingresa un número: '))
print(multiplo_de_cinco(number))