# FIND THE FIRST NON-REPEATING CHARACTER
    # Given a string, find the first non-repeated character.

input_str = "rishabkumarlovejanemargolis"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("The first non-repeating character is:", char)
        break