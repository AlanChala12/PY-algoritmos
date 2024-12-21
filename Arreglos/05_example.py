# Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces está repetido el mayor.
enteros = []
contador = 0

for i in range(1, 11):
  numeros = int(input(f'Entero {i}: '))
  enteros.append(numeros)

numero_mayor = max(enteros)

for x in enteros:
    if x == numero_mayor:
        contador += 1
    
print(f'El número {numero_mayor} que es el número mayor se encuentra {contador} vez/veces')