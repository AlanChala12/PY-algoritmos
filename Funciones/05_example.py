# Construir una función que reciba como parámetro un entero y retorne el primer dígito de este entero.
entero = int(input('Entero: '))

def primer_digito(n):
  if n < 10:
    return n

  elif 10 <= n < 100:
    return n // 10

  elif 100 <= n < 1000:
    return n // 100

  elif 1000 <= n < 10000:
    return n // 1000
  
  else:
    return 'Ingresa un número de cuatro dígitos o menos'

result = primer_digito(entero)
print(result)