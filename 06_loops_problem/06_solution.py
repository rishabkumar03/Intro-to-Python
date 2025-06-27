# TRANSPORTATION MODE SELECTION 
    # Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car)

distance = 3

if distance < 3:
    transportation = "Walk"
elif distance <= 15:
    transportation = "Bike"
else:
    transportation = "Car"

print("RISHAB recommends you to use", transportation)