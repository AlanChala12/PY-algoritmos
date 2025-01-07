# Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne la cantidad de números terminados en 3 que contiene el vector.

def terminados_en_tres(vector):  
  cantidad = 0
  
  for i in vector:
    if i % 10 == 3:
      cantidad += 1

  if cantidad == 0:
    return f'No se encontraron números que terminaran en 3'
  else:
    return f'La cantidad de números que terminan en 3 del vector {vector}, es de: {cantidad}'

try:
  numeros = [int(input(f'Entero {i + 1}: ')) for i in range(10)]
  print(terminados_en_tres(numeros))
  
except ValueError:
  print('**Por favor, ingresa valores numéricos**')
