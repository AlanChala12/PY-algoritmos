# Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces en el vector se encuentra el dígito 2

enteros = [ int(input(f'Entero {i + 1}: ')) for i in range(10) ]
apariciones = 0

for i in enteros:
    num = str( i )
    apariciones += num.count('2')
    
print(f'El dígito 2 se encuentra { apariciones } vez/veces en el vector.')