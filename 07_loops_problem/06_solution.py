# FACTORIAL CALCULATOR
    # Compute the factorial of a number using a while loop.

number = 3
input_num = number
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1

    factorial *= number
    number -= 1

print("The factorial of", input_num, "is:", factorial)