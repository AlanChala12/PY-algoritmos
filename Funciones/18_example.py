# Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne la posición en la cual se encuentra el mayor de los datos del vector.

numeros = []

for i in range(1, 11):
  numero = int(input(f'Entero {i}: '))
  numeros.append(numero)

def indice_del_valor_mayor(vector):

  numero_mayor = max(vector)
  indice = vector.index(numero_mayor) + 1
  
  return f'El mayor de los datos "{numero_mayor}" se encuentra en el índice "{indice}" del vector {numeros}'

print(indice_del_valor_mayor(numeros))