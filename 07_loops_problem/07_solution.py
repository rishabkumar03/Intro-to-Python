# VALIDATE INPUT 
    # Keep asking the user for input until they enter a number between 1 to 10.

while True :
    number = int(input("Enter the value between 1 to 10: "))
    if 1 <= number <= 10:
        print("Thankyou for following guidelines")
        break
    else:
        print("Try again")