# Leer 10 números enteros, almacenarlos en un vector y determinar si el promedio entero de dichos números es un número primo.
enteros = []
sum_digitos = 0
n = 10

for i in range(1, 11):
  numeros = int(input(f'Entero {i}: '))
  enteros.append(numeros) 

for x in enteros:
  sum_digitos = sum_digitos + x

promedio = sum_digitos // n

is_primo = True
for primo in range(2, promedio):
  if promedio % primo == 0:
    is_primo = False
    break

if is_primo == True and is_primo > 1:
  print(f'El promedio entero {promedio} del vector {enteros}, es un número ¡PRIMO!')

else:
  print(f'El promedio entero {promedio} del vector {enteros}, no es un número ¡PRIMO!')