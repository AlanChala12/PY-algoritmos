# Leer 10 números enteros, almacenarlos en un vector y determinar cuáles son los datos almacenados múltiplos de 3.

numeros = [int(input(f'Entero {i + 1}: ')) for i in range(10)]
mtpls_de_tres = [x for x in numeros if x % 3 == 0]

print(f'Los múltiplos de tres del vector {numeros}, son: {mtpls_de_tres}')