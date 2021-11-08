##---------------------------------------------------------------------
## CODERHOUSE
##  Student     : AVERO, Patricio
##  Course      : Python
##  Commission  : 23855
##  Tutor       : ZUAZO, Joaquín
##  Class       : 01
##  Date        : 27-OCT-2021
##  Note        : Meant to manage floating point with two decimals precision
##---------------------------------------------------------------------

## Variables
# Set by standard input
grade_1=input("Insert the 1st grade: ")
grade_2=input("Insert the 2nd grade: ")

# Fixed variables (either way, can be changed by editting here)
grade_1_weight=0.4
grade_2_weight=0.6

## Main
# 1st grade after weight
grade_1_aw=(float(grade_1)*grade_1_weight)

# 2nd grade fater weight
grade_2_aw=(float(grade_2)*grade_2_weight)

# Final grade calculation
final_grade=grade_1_aw+grade_2_aw

# Print to standard output
print("--------------------------------------------------")
print("1st grade after weight (",grade_1_weight*100,"%) [1]\t: ", format(grade_1_aw,".2f"))
print("2nd grade after weight (",grade_2_weight*100,"%) [2]\t: ", format(grade_2_aw,".2f"))
print("The final grade is [1]+[2]\t\t: ", format(final_grade,".2f"))
