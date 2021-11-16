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

## Inser the times of numbers to enter
times = int(input("Enter how many number you want to average: "))

## Loop all over the times entered
res = float(0)
for time in range(1, times+1, 1):
    num = float(input(f"Enter the {time} number:"))
    res = res + num

## Average
print(f"The average of the {times} numbers is: ", res / times)
