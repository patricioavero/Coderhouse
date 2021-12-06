##---------------------------------------------------------------------
## CODERHOUSE
##  Student     : AVERO, Patricio
##  Course      : Python
##  Commission  : 23855
##  Tutor       : ZUAZO, Joaquín
##  Class       : 10
##  Date        : 30-NOV-2021
##  Challenge   : https://docs.google.com/document/d/1LUAVUvZATKuzSOTLacwcaB0Z84tg_Acy33XfzowMoK4/edit
##  Notes       : 
##---------------------------------------------------------------------

## Imports
import os
import math

## Functions
# To clear the screen
def clear_screen():
    os_name = os.name
    if (os_name.lower() == 'posix'):
        os.system('clear')
    elif (os_name.lower() == 'nt'):
        os.system('cls')

# Validate ENTER key
def ask_for_number():
    

# Validate integer
def validate_int(num, message):
    if num.isnumeric() == False:
        num = input(message)


    
# Rectangle's area calculation
def rectangle_area(base, height):
    r_area = base * height
    return r_area

#Circle's area
def circule_area(radius):
    c_area = math.pi * radius**2
    return c_area

# Relation comparison
def comparison(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0



## Rectangle
clear_screen()
print("Desafío entregable 3.1")
print("----------------------")
base = int(input("Enter the rectangle's base: "))
altura = int(input("Enter the rectangle's height: "))
rectangle_area = rectangle_area(base, altura)
print(f"The rectangle's area is: {rectangle_area}")
validate_enter()


## Circle
clear_screen()
print("Desafío entregable 3.2")
print("----------------------")
radius = int(input("Enter the radius of the circule: "))
circule_area = circule_area(radius)
print(f"The area of the circule is: {circule_area}")
validate_enter()

## Relation
clear_screen()
print("Desafío entregable 3.3")
print("----------------------")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2ns number: "))
comp_result = comparison(num1, num2)

if comp_result == 1:
    print(f"The Num 1: \'{num1}\' is greater than Num 2: \'{num2}\'")
elif comp_result == -1:
    print(f"The Num 1: \'{num1}\' is less than Num 2: \'{num2}\'")
else:
    print(f"The Num 1: \'{num1}\' and Num 2: \'{num2}\' are equal")

validate_enter()

validate_int(num = "a", message = "Please enter a number: ")