# Cree una función que determine si un año es bisiesto 

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 400 == 0:
            leap = True
    
    return leap

year = int(input("Year: "))
print(is_leap(year))