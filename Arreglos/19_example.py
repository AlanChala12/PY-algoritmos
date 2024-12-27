# Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces en el vector se encuentra el dígito 2.
enteros = []
cantidad_de_dos = 0

for i in range(1, 11):
    numero = int(input(f'Entero {i}: '))
    enteros.append(numero) 

for x in enteros:
    conver = str(x)
    cantidad_de_dos += conver.count('2')

print(f'El dígito 2 se encuentra {cantidad_de_dos} vez/veces en el vector.')
print(enteros)