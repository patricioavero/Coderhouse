import sys
import os

script_name = sys.argv[0]
os_name = os.name

if (os_name.lower() == 'posix'):
    os.system('clear')
elif (os_name.lower() == 'nt'):
    os.system('cls')

if (len(sys.argv) < 3):
    print("This script uses two grades as arguments to work")
    print
    print("python {script_anme} <ARG_1> <ARG_2>")
elif (0 <= int(sys.argv[1]) <= 10) and (0 <= int(sys.argv[2]) <= 10):
	grade_1 = int(sys.argv[1])
	grade_2 = int(sys.argv[2])
	if (grade_1 >= 7 ) and (grade_2 >= 7):
	    print("You have been exempted from final exam. Congrats!")
	elif (grade_1 >= 4) and (grade_2 >= 4):
	    print("You have approved the couse")
	elif (grade_1 < 4) and (grade_2 < 4):
	    print("You will have to repeat this course")
	elif (grade_1 < 4) or (grade_2 < 4):
	    print("You have not reached the minimum to approve the course")
	    if (grade_1 < 4):
		    print("You must repeat the 1st exam only")
	    else:
		    print("You must repeat the 2nd exam only")
else:
    print("Values for grades must be from 0 to 10 (inclusive)")
