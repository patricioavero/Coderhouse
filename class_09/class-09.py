##---------------------------------------------------------------------
## CODERHOUSE
##  Student     : AVERO, Patricio
##  Course      : Python
##  Commission  : 23855
##  Tutor       : ZUAZO, Joaquín
##  Class       : 09
##  Date        : 22-NOV-2021, 24-NOV-2021
##  Challenge   : https://docs.google.com/presentation/d/1PbUtfvt9M7oQzSm07rM759PAxwaDweR87g6GAqyNWuk/preview#slide=id.ged1c8e7111_1_60
##  Notes       : 
##---------------------------------------------------------------------

##----------------------------------------
## Imports
##----------------------------------------
import os

##----------------------------------------
## Variables
##----------------------------------------
option = str('y')

##----------------------------------------
## Functions
##----------------------------------------
# To clear the screen
def clear_screen ():
    os_name = os.name
    if (os_name.lower() == 'posix'):
        os.system('clear')
    elif (os_name.lower() == 'nt'):
        os.system('cls')

# To print the menu
def menu ():
    print("*** Lepar-Year Checker ***")
    year = int(input("Enter the year you want to check ---> "))
    return year

# To check if programs continues
def quit ():
    option = str(input("Do you want to check another year? [y/n]) "))
    return option

# To evaluate divisor number
def divisor (dividend, divisor):
    quotient = dividend % divisor
    if (quotient == 0):
        return 1 
    else:
        return 0

# To check if the year is leap-year or not
def leap_or_not (year):
    if divisor(year, 4):
        leap_condition = 1
        if divisor(year, 100):
            leap_condition = 0
            if divisor(year, 400):
                leap_condition = 1
    else:
        leap_condition = 0
    
    if leap_condition == 1:
        return (1, year)
    if leap_condition == 0:
        return (0, year)

# To print the message on STDOUT 
def print_leap (leap_bool):
    if leap_bool[0] == 1:
        print(f"The year {leap_bool[1]} IS a leap-year")
    else:
        print(f"The year {leap_bool[1]} IS NOT a leap-year")
        
##----------------------------------------
## Main
##----------------------------------------
while option.lower() == 'y':
    clear_screen()
    print_leap(leap_or_not(menu()))
    option = quit()
