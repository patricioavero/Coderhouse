## Class 03
## In-Class Exercise

name= str(input("What's your name? "))
preference = str(input("Which one do you prefer? (Marvel or Capcom) "))

if (preference.lower() == 'marvel' and name[0].upper() < 'M') or (preference.lower() == 'capcom' and name[0].upper() > 'N'):
	print(name, "your groups is: A")
else:
	print(name, "your group is: B")
