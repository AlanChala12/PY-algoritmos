# Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x e y leídos.
x = int(input('Ingresa un número entero: '))

multiplos_dos = 0
cantidad_multiplos_dos = 0
promedio_dos = 0

multiplos_cinco = 0
cantidad_multiplos_cinco = 0
promedio_cinco = 0

for y in range(1, x + 1):

  if y % 2 == 0:
    multiplos_dos = multiplos_dos + y
    cantidad_multiplos_dos += 1

  elif y % 5 == 0:
    multiplos_cinco = multiplos_cinco + y
    cantidad_multiplos_cinco += 1

#Calculo de promedios.
promedio_dos = multiplos_dos // cantidad_multiplos_dos
promedio_cinco = multiplos_cinco // cantidad_multiplos_cinco

if promedio_dos > promedio_cinco:
  print('---El promedio de los múltiplos de dos, es mayor al promedio de los múltiplos de cinco---')
elif promedio_cinco > promedio_dos:
    print('---El promedio de los múltiplos de cinco, es mayor al promedio de los múltiplos de dos---')
else:
  print('---El promedio de los múltiplos de dos, es igual al promedio de los mútiplos de cinco---')

