# Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números tienen, de los almacenados allí, menos de 3 dígitos.
numeros = [ int(input(f'Entero { i + 1 }: ')) for i in range(10) ]
contador = 0
    
for x in numeros:
    if x < 100:
        contador += 1
        
print(f'Los números almacenados que tienen menos de 3 dígitos, son {contador}.')
print(numeros)