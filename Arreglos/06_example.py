# Leer 10 números enteros, almacenarlos en un vector y calcularle el factorial a cada uno de los números leídos almacenándolos en otro vector.

numeros = [ int(input(f'Entero { y + 1 }: ')) for y in range(10) ]
factoriales = []

for iterador in numeros:
    x = iterador
    factorial = x
    
    for i in range( 1, x ):
        factorial = factorial * i
        
    factoriales.append(factorial)
    
print(factoriales)