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

## The given lists
list_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
list_2 = ["h",'o','l','a',' ', 'l','u','n','a']

## The lists
list_3 = []
list_tmp = []

## Loop to the the first list and its duplicated items
## A new list named list_3 will have only the duplicated items
for item in list_1:
    if item not in list_tmp:
        list_tmp.append(item)
    else:
        list_3.append(item)

## New loop to do the same over the second list named list_2
## The list already created for duplicate items will also have the list_2 dups
list_tmp = []
for item in list_2:
    if (item not in list_tmp):
        list_tmp.append(item)
    else:
        list_3.append(item)

## Print the resultant list_3
## In here you will only have: (dups on list 1 + dups on list 2) without dups between them.
print(f"The 3rd list has the following elements: {list_3}")
