# Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne el promedio entero del vector.

def promedio_entero(vector):
    sumatoria_de_valores = sum(vector)
    promedio = sumatoria_de_valores // len(vector)
    return f'El promedio entero del vector {vector} es de: {promedio}.'

try:
    numeros = [int(input(f'Entero {i + 1}: ')) for i in range(10)]
    print(promedio_entero(numeros))

except ValueError:
    print('Por favor, ingresa valores numéricos válidos')