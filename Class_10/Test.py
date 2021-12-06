# Validate a float
def float_validation(float(f_num)):
    print(type(f_num))
    if type(f_num) != 'float':
        print("It is not a float number")
    else:
        print("FLOAT!")

num = '3.4'
print(type(float(num)))
float_validation(num)