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
## Preset the num variable
num = int(0)
counter = int(0)

## Insert the number to evaluate
while (num % 2 == 0):
    num = int(input("Enter an odd number: "))
    if (num %2 != 0 and counter == 0):
        print(f'The number {num} is odd, you hit center in the first attempt.')
    elif (num % 2 == 0):
        print("The number you have entered is even, please enter again")
        counter += 1
    elif (counter == 1):
        print("OK, it seems that you are checking this program... you have entered an even number only one time.")
    elif (counter > 1):
        print(f"Finally, you've tried {counter} times !!! I almost send you to school again...")
        break
