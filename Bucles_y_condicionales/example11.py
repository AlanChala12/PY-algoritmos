# Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número n leído.
x = int(input('Ingresa un número: '))
promedio = 0
contador_de_multiplos = 0

for y in range(1, x + 1):

  if y % 3 == 0:
    contador_de_multiplos += 1
    promedio = promedio + y

promedio = promedio // contador_de_multiplos

print(f'El promedio de los primeros múltiplos de tres, es de {promedio}.')