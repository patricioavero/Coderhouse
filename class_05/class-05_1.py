##---------------------------------------------------------------------
## CODERHOUSE
##  Student     : AVERO, Patricio
##  Course      : Python
##  Commission  : 23855
##  Tutor       : ZUAZO, Joaquín
##  Class       : 05
##  Date        : 08-NOV-2021 & 10-NOV_2021
##  Challenge   : https://docs.google.com/document/d/1_U-mHyF6nTwHJrHsgWt9oUQ-WIDz_mdcKIC97r6W3o4/edit
##  Notes       : 
##---------------------------------------------------------------------

## Variables
option = ''
valid_options = (1, 2, 3, 4, 'e')
calc_menu = """

\t\t\tMENU

\t[1]. Add the two numbers you have entered
\t[2]. Substract the two numbers you have entered
\t[3]. Multiply the two numbers you have entered
\t[4]. Divide the two numbers you have entered

\t[q]. Quit

"""

## Ask for two numbers
num1 = str(input("Enter the 1st number: "))
num2 = str(input("Enter the 2nd number: "))

## Loop the menu for valid options
while (option not in valid_options):
    print(calc_menu)
    option = input("Enter your choice: ")
    
    if (option == '1'):
        result = int(num1) + int(num2)
        print(f'The result of {num1} + {num2} is: {result}')
    elif (option == '2'):
        result = int(num1) - int(num2)
        print(f'The result of {num1} - {num2} is: {result}')
    elif (option == '3'):
        result = int(num1) * int(num2)
        print(f'The result of {num1} x {num2} is: {result}')
    elif (option == '4'):
        result = int(num1) / int(num2)
        print(f'The result of {num1} / {num2} is: {result}')
    elif (option.lower() == 'q'):
        break

    input("Please, press <Enter> to continue...")
