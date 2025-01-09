# Construir una función que reciba como parámetros un vector de 10 posiciones enteras y un dígito y que retorne la cantidad de veces que dicho dígito se encuentra en el vector.

def aparaciones(vector, digito):
    cantidad_de_apariciones = 0
    digito = str(digito)
    
    for i in vector:
        cadena = str(i)
        cantidad_de_apariciones = cadena.count(digito) + cantidad_de_apariciones
        
    return f'El dígito {digito} se encuentra {cantidad_de_apariciones} vez/veces en el vector {vector}'
        

try:
    numeros = [int(input(f'Entero {i + 1}: ')) for i in range(10)]
    digito = int(input('Ingresa un número dígito [0-9]: '))

    if digito < 0 or digito > 9:
        print('Por favor ingresa un dígito entre 0 y 9')
    else:
        print(aparaciones(numeros, digito))
  
except ValueError:
    print('**Por favor, ingresa valores numéricos**')


