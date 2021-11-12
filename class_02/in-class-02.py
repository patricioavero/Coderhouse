# Lists predefined
list_1 = [1, 12, 123]
print("0. The original list 1: ", list_1)
list_2 = ["bye", "ciao", "Agur", "Adieu"]
print("0. The original list 2: ", list_2)
print("---------------------------------------------------------")

# 1
list_1.append(1234)
list_1.append("Hola")
print("1. list 1 after #1: ", list_1)
print("--")

# 2
list_2.append("Hola")
list_2.append(1234)
print("2. list 2 after #2: ", list_2)
print("--")


# 3
list_1.pop()
list_3 = list_1
print("3. list 3 :", list_3)
print("--")

# 4
list_4 = list_2[1:3]
print("4. list 4: ", list_4)
print("--")

# 5
list_5 = list_3 + list_4
print("5. list 5: ", list_5)
print("--")
