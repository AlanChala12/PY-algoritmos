# Leer 10 números enteros, almacenarlos en un vector. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en el vector.

try: 
    numeros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
    entero = int(input('Ingresa un número entero: '))
    divisores_exactos = 0
    
    for x in numeros:
        if entero % x == 0:
            divisores_exactos += 1
            
    print(f'Los divisores exactos del número {entero} que están en el vector {numeros}, son: {divisores_exactos}')

    
except ValueError:
    print('Por favor, ingresa valores numéricos')
    