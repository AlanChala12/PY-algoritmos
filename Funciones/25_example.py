# Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne la posición del número entero que tenga mayor cantidad de dígitos.

def numero_mayor(vector):
  max_num = max(vector)
  indice = vector.index(max_num)
  return f'El número con la mayor cantidad de dígitos en el vector {vector}, se encuentra en la posición {indice + 1}'

numeros = [int(input(f'Entero {i + 1}: ')) for i in range(10)]
print(numero_mayor(numeros))