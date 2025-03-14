# Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5.
entero = int(input('Entero: '))
promedio = 0
terminados_en_cinco = 0
cantidad = 0

for x in range(entero, -1, -1):
  
  if x % 10 == 5:
    terminados_en_cinco = terminados_en_cinco + x
    cantidad += 1

promedio = terminados_en_cinco // cantidad
print(f'El promedio de los números terminados en cinco, es de: {promedio}%')