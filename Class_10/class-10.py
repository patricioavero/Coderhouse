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
    num = ''
    if num.isnumeric() != True:
        valid = 1
        while valid == 1:
            num = input(msg)
            if num.isnumeric() == True:
                valid = 0
    return int(num)

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
    average = (float(num1) + float(num2)) / 2
    return float(average)

# Cut
def cut_number(lower_limit, num, upper_limit):
    if lower_limit < num < upper_limit:
        return num
    elif num < lower_limit:
        return lower_limit
    else:
        return upper_limit

# Separate odd and even numbers
def separate(list_1):
    list_1.sort()
    list_even = []
    list_odd = []
    for num in list_1:
        if num % 2 == 0:
            list_even.append(num)
        else:
            list_odd.append(num)
    return[list_even, list_odd]

####################################################################
## Main
####################################################################
## Rectangle
clear_screen()
print("Desafío entregable 3.1: Rectangle Area")
print("--------------------------------------")
base = ask_until_number("Enter the rectangle's base: ")
altura = ask_until_number("Enter the rectangle's height: ")
rectangle_area = rectangle_area(base, altura)
print(f"The rectangle's area is: {rectangle_area}")
validate_enter()


## Circle
clear_screen()
print("Desafío entregable 3.2: Circule Area")
print("------------------------------------")
radius = ask_until_number("Enter the radius of the circule: ")
circule_area = circule_area(radius)
print(f"The area of the circule is: {circule_area}")
validate_enter()

## Relation
clear_screen()
print("Desafío entregable 3.3: Relation")
print("--------------------------------")
num1 = ask_until_number("Enter the 1st number: ")
num2 = ask_until_number("Enter the 2nd number: ")
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
print("-------------------------------")
num1 = ask_until_number("Enter the 1st number: ")
num2 = ask_until_number("Enter the 2nd number: ")
print(f"The average of {num1} and {num2} is:", average(float(num1), float(num2)))
validate_enter()

## Cut
clear_screen()
print("Desafío entregable 3.5: Cut")
print("---------------------------")
upper_limit = 10
lower_limit = 0
num = ask_until_number("Enter the number to cut: ")
print(f"The number to print is: {cut_number(lower_limit, num, upper_limit)}")
validate_enter()

## Separation
clear_screen()
print("Desafío entregable 3.6: Separate odd and even")
print("---------------------------------------------")
list_1 = [9, 6, 7, 0, 2, 3, 8, 5, 6, 0, 3, 8, 6, 2, 1, 9, 6, 0]
result = separate(list_1)
print(f"The even list is: {result[0]}")
print(f"The odd list is: {result[1]}")
validate_enter()