# Leer tres números enteros y determinar si el penúltimo dígito de los tres números es igual.
number1 = int(input('Primer entero: '))
number2 = int(input('Segundo entero: '))
number3 = int(input('Tercer entero: '))

if number1 < 10 and number2 < 10 and number3 < 10:
    print(f'Ambos números son iguales')
    
elif 10 <= number1 < 100 and 10 <= number2 < 100 and 10 <= number3 < 100:
    dig1_number1 = number1 // 10
    dig2_number2 = number2 // 10
    dig3_number3 = number3 // 10
    
    condicion = dig1_number1 == dig2_number2 == dig3_number3
    
    if condicion:
        print(f'Los penúltimos dígitos de los números {number1}, {number2} y {number3} son iguales')
    
elif 100 <= number1 < 1000 and 100 <= number2 < 1000 and 100 <= number3 < 1000:
    dig1_number1 = (number1 // 10) % 10
    dig2_number2 = (number2 // 10) % 10
    dig3_number3 = (number3 // 10) % 10
    
    condicion1 = dig1_number1 == dig2_number2 == dig3_number3
    
    if condicion1:
        print(f'Los penúltimos dígitos de los números {number1}, {number2} y {number3} son iguales')
        
else:
    print(f'Proporciona números que contenga la misma cantidad de dígitos')