# Leer 10 números enteros, almacenarlos en un vector y determinar a cuántos es igual el cuadrado de cada uno de los números leídos.

try:
    numeros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
    cuadrados = []

    for x in numeros:
        cuadrados.append(x ** 2)
        
    print(f'El cuadrado de cada uno de los números leídos, es de: {cuadrados}')
    
except ValueError:
    print('Por favor, ingresa valores numéricos')
    