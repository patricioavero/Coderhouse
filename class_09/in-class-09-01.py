def odd_or_even (num):
    if type(num) == int:
        if int(num) % 2 == 0:
            msg='Even'
        else:
            msg='Odd'
    else:
        msg="Please insert a number."

    return msg

num = [1, 'a', 4, 'Hola']

for item in num:
    print(odd_or_even(num))


