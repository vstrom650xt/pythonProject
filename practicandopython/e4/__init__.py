number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))

if number1 > number2:
    greater = number1
    smaller = number2
elif number2 > number1:
    greater = number2
    smaller = number1
else:
    print("The numbers are equal. It cannot be determined if one is a multiple of the other.")
    exit()

if greater % smaller == 0:
    print(f"{greater} is a multiple of {smaller}.")
else:
    print(f"{greater} is not a multiple of {smaller}.")