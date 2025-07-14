file = open('youtube.txt', 'w')

try:
    file.write('Guss Fringg')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('Guss Fringg')