# PET FOOD RECOMMENDATION
    # Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)

pet_species = "Dog"
pet_age = 3

if pet_species == "Dog":
    if pet_age < 2:
        print("Food should be Puppy food")
    else:
        print("Food should be Normal Dog Food")
elif pet_species == "Cat":
    if pet_age > 5:
        print("Food should be Senior Cat Food")
    else: 
        print("Food should be Normal Cat Food")
else:
    print("Enter either Dog or Cat")
