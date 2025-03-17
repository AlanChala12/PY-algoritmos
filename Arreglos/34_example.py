# Dada un conjunto de estudiantes, determinar el promedio de notas de un estudiante es especifico.

student_marks = {
    'Krishna':[ 67, 68, 69 ],
    'Arjun': [ 70, 98, 63 ],
    'Malika': [ 52, 56, 60 ]
}

student = input('Ingresa el nombre del estudiante: ')

average = sum(student_marks[student]) / len(student_marks[student])
print( f'{average:.2f}' )