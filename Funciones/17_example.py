# Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne el mayor de los datos del vector.
numeros = []

for i in range(1, 11):
    numero = int(input(f'Entero {i}: '))
    numeros.append(numero)

def numero_mayor(vector):
    valor_maximo = max(vector)
    return valor_maximo

print(f'El mayor de todos los datos del vector {numeros} es "{numero_mayor(numeros)}"')