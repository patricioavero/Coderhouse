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


# Function to evaluate divisor number
def divisor (dividend, divisor):
    quotient = dividend % divisor
    if (quotient == 0):
        return (True, quotient)
    else:
        return (False, quotient)

print(divisor(973977, 5453))
