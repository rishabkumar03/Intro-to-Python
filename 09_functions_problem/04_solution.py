# FUNCTION RETURNING MULTIPLE VALUES
    # Create a function that returns both the area and circumference of a cicle given its radius.

import math

def circle_measurement(radius):
    area = round(math.pi, 2)  * (radius ** 2)
    circumference = 2 * round(math.pi, 2) * radius

    return area, circumference 

a, c = circle_measurement(3)

print("Area of circle is:", a )
print("Circumference of circle is:", c)