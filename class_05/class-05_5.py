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

# The given list
nums =  [1, 3, 6, 9]

## Ask the user to guess one of the numbers in the list
# Set the initial condicion for the loop
num_user = int(0)
# The loop itself.
while (num_user not in nums):
    num_user = int(input("Guess on number that is in the list: "))
else:
    print(f"well done, the number {num_user} is in the list --->  {nums}")
