# Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos.

number = int(input('Ingresa un número entero: '))

if number < 10:
    print(f'La suma de {number} es: {number}')
    

elif number >= 10 and number < 100:
    dig1 = int(number / 10)
    
    dig2 = int(number / 10) * 10
    dig2 = number - dig2
    
    result = dig1 + dig2
    print(f'La suma de los dígitos del número {number} es: {result}')


elif number >= 100 and number < 1000:
    
    ultimo_digito = int(number / 10) * 10
    ultimo_digito = number - ultimo_digito

    total = int(number / 10) 
    
    segundo_digito = int(total / 10) * 10
    segundo_digito = total - segundo_digito

    primer_digito = int(total / 10)
    
    result2 = ultimo_digito + segundo_digito + primer_digito
    print(f'La suma de los dígitos del número {number} es: {result2}')
    
else:
    print(f'!ERROR¡ el número proporcionado es muy grande.')   