##---------------------------------------------------------------------
## CODERHOUSE
##  Student     : AVERO, Patricio
##  Course      : Python
##  Commission  : 23855
##  Tutor       : ZUAZO, Joaquín
##  Class       : 02
##  Date        : 01-NOV-2021
##  Challenge   : https://docs.google.com/document/d/1ZY65N_5J4KJt-Ecdrp_HV9NhyvSZQLoYKhk8bNwEirU/edit
##  Notes       :               
##                #4 there is a reuse of the Class01's deliverable challenge
##---------------------------------------------------------------------

## [1]
print("--------------------------------------------------")
print('--- #1 ---')
print("--------------------------------------------------")
print('"Hola Mundo" \t\tis a String')
print('[1, 10, 100] \t\tis a List')
print('-25 \t\t\tis a Integer')
print('(8, 100, 12) \t\tis a Tuple')
print('1.167 \t\t\tis a Float')
print('["Hola", "Mundo"] \tis a List')
print("' ' \t\t\tis a String")
print('(1, -5, "Hola!") \tis a Tuple')
print("--------------------------------------------------")
print()

##2
print("--------------------------------------------------")
print('--- #2 ---')
print("--------------------------------------------------")
print('print(a * 5) \t\t= -25')
print('print(a - b) \t\t= 5')
print('print(c + "Mundo") \t= HolaMundo')
print('print(c * 2) \t\t= HolaHola')
print('print(c[-1]) \t\t= a')
print('print(c[1:]) \t\t= ola')
print('print(d + d) \t\t= [1, 2, 3, 1, 2, 3]')
print('print(e[1]) \t\t= 5')
print('print(e+(7,8,9)) \t= (4, 5, 6 ,7 ,8 ,9)')
print()

## [3]
print("--------------------------------------------------")
print('--- #3 ---')
print("--------------------------------------------------")
print("""
1. numero_1 = 9
2. numero_2 = 3
3. numero_3 = 6
4. ​
5. media = numero_1 + numero_2 + numero_3 / 3
6. print("La nota media es", media)
7. La nota media es 14.0
""")
print("""
Answer: 
\tline 5 should be like this ---> media = (numero_1 + numero_2 + numero_3) / 3
""")

## [4]
print("--------------------------------------------------")
print('--- #4 ---')
print("--------------------------------------------------")
## Variables
# Set by standard input
grade_1 = input("Insert the 1st grade: ")
grade_2 = input("Insert the 2nd grade: ")
grade_3 = input("Insert the 3rd grade: ")

# Fixed variables (either way, can be changed by editting here)
grade_1_weight = 0.15
grade_2_weight = 0.35
grade_3_weight = 0.50

## Main
# 1st grade after weight
grade_1_aw = (float(grade_1) * grade_1_weight)

# 2nd grade after weight
grade_2_aw = (float(grade_2) * grade_2_weight)

# 2nd grade after weight
grade_3_aw = (float(grade_3) * grade_3_weight)

# Final grade calculation
final_grade = grade_1_aw + grade_2_aw + grade_3_aw

# Print to standard output
print("--------------------------------------------------")
print("1st grade after weight (", grade_1_weight * 100, "%) [1]\t: ", format(grade_1_aw, ".2f"))
print("2nd grade after weight (", grade_2_weight * 100, "%) [2]\t: ", format(grade_2_aw, ".2f"))
print("3rd grade after weight (", grade_3_weight * 100, "%) [3]\t: ", format(grade_3_aw, ".2f"))
print("--------------------------------------------------")
print("The final grade is [1] + [2] + [3]\t: ", format(final_grade,".2f"))
print("--------------------------------------------------")

## [5]
print("--------------------------------------------------")
print('--- #5 ---')
print("--------------------------------------------------")
## Variables
# The given matrix
matrix = [ 
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]
# Print the matrix to see the original values
print("The source matrix is\t: ", matrix)

# Fourth number calculation (all over the lists)
list_1_forth_number=sum(matrix[0])
list_2_forth_number=sum(matrix[1])
list_3_forth_number=sum(matrix[2])
list_4_forth_number=sum(matrix[3])

# Append the forth number to each list
matrix[0].append(list_1_forth_number)
matrix[1].append(list_2_forth_number)
matrix[2].append(list_3_forth_number)
matrix[3].append(list_4_forth_number)

# Print to standard out the resultant matrix
print("The resultant matrix is\t: ", matrix)
