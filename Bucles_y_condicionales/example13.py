#Leer dos números enteros y mostrar todos los múltiplos de 5 comprendidos entre el menor y el mayor.
x = int(input('Ingresa un número entero: '))
y = int(input('Ingresa otro número entero: '))

entero_menor = min(x, y)
entero_mayor = max(x, y)

print('--Los múltiplos de cinco son--')

for z in range(entero_menor, entero_mayor + 1):

  if z % 5 == 0:
    print(z)
