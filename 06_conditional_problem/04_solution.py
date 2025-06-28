# FRUIT RIPENESS CHECKER
    # Determine if a fruit is ripe, overipe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = "Green"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    else:
        print("Please enter valid color")
