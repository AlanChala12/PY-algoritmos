import random

print('¡ADIVINA EL NÚMERO SECRETO!')

def numero_aleatorio():
    num = random.randrange( 1, 11 )
    return num
    
intentos = 5
numero_secreto = numero_aleatorio()

while intentos != 0:
    
    numero_de_usuario = int( input('Ingresa un número entero entre [1-10]: ') )
    if numero_de_usuario == numero_secreto:
        print(f'Felicidades, adivinaste el número secreto "{numero_secreto}"')
        break
    
    if numero_de_usuario > numero_secreto:
        print('--PISTA--')
        print('El número secreto es MENOR')
        intentos -= 1
        print(f'Te restan {intentos} intento/s')
        print()
        
    if numero_de_usuario < numero_secreto:
        print('--PISTA--')
        print('El número secreto es MAYOR')
        intentos -= 1
        print(f'Te restan {intentos} intento/s')
        print()    
