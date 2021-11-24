import sys
import os

script_name = sys.argv[0]
os_name = os.name

if (os_name.lower() == 'posix'):
    os.system('clear')
elif (os_name.lower() == 'nt'):
    os.system('cls')

if (len(sys.argv) < 3):
    print("This script uses two notes as arguments to work")
    print
    print("python {script_anme} <ARG_1> <ARG_2>")
elif (0 <= int(sys.argv[1]) <= 10) and (0 <= int(sys.argv[2]) <= 10):
	grade_1 = int(sys.argv[1])
	grade_2 = int(sys.argv[2])
	if (grade_1 >= 7 ) and (grade_2 >= 7):
	    print("You have promoted the course")
	elif (grade_1 >= 4) and (grade_2 >= 4):
	    print("You have approved the couse")
	elif (grade_1 < 4) and (grade_2 < 4):
	    print("You will have to repeat this course")
	elif (grade_1 < 4) or (grade_2 < 4):
	    print("You have not reched the minimum to approve the course")
else:
    print("Values for grades should be from 0 to 10 (inclusive)")
