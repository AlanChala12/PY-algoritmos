# Dada la hoja de puntuación de los participantes de su Día del Deporte Universitario, se le pide que encuentre la puntuación del segundo lugar.

arr = [ 2, 3, 6, 6, 5 ]
arr_tidy = sorted( arr )
new_arr = []

for i in arr_tidy:
  if i == max(arr_tidy): 
    break
  new_arr.append(i)

runner_up = max( new_arr )
print( runner_up )