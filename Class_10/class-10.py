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
def validate_enter():
    key = 1
    while key != "":
        key = input("Press ENTER to continue...")

def ask_until_number(msg):
    num = 'a'
    if num.isnumeric() != True:
        valid = 1
        while valid == 1:
            num = input(msg)
            float(num)
            if num.isnumeric() == True:
                valid = 0
    return float(num)

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

# Average
def average(num1, num2):
    average = (num2 + num2) / 2
    return float(average)


## Rectangle
clear_screen()
print("Desafío entregable 3.1: Rectangle Area")
print("----------------------")
base = ask_until_number("Enter the rectangle's base: ")
altura = ask_until_number("Enter the rectangle's height: ")
rectangle_area = rectangle_area(base, altura)
print(f"The rectangle's area is: {rectangle_area}")
validate_enter()


## Circle
clear_screen()
print("Desafío entregable 3.2: Circule Area")
print("----------------------")
radius = ask_until_number("Enter the radius of the circule: ")
circule_area = circule_area(radius)
print(f"The area of the circule is: {circule_area}")
validate_enter()

## Relation
clear_screen()
print("Desafío entregable 3.3: Relation")
print("----------------------")
num1 = ask_until_number("Enter the 1st number: ")
num2 = ask_until_number("Enter the 2ns number: ")
comp_result = comparison(num1, num2)
if comp_result == 1:
    print(f"The Num 1: \'{num1}\' is greater than Num 2: \'{num2}\'")
elif comp_result == -1:
    print(f"The Num 1: \'{num1}\' is less than Num 2: \'{num2}\'")
else:
    print(f"The Num 1: \'{num1}\' and Num 2: \'{num2}\' are equal")
validate_enter()

## Average
clear_screen()
print("Desafío entregable 3.4: Average")
print("----------------------")
num1 = ask_until_number("Enter the 1st number: ")
num2 = ask_until_number("Enter the 2ns number: ")
print(f"The average of {num1} and {num2} is:", average(num1, num2))
validate_enter()