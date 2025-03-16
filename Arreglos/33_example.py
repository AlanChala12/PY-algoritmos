# Imprima el nombre de cualquier estudiante que tenga la segunda calificación más baja. Si hay varios estudiantes, ordene sus nombres alfabéticamente e imprima cada uno en una nueva línea.

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
grades = sorted([ i[1] for i in students  ])
grades2 = []

for i in grades:
  if i == min(grades):
    continue
  else:
    grades2.append(i)

second_min_grade = min(grades2)
names = []

for x in students:
  if x[1] == second_min_grade:
    names.append(x[0])

tidy_names = sorted(names)

for z in tidy_names:
  print( z )