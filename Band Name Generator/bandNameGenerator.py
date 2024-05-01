import random
 

def bandNameGenerator():
    print("Welcome to the Band Name Generator")
    print("What's the name of the city you grew up in? ")
    cityName = input("Enter Name: ")
    print("If you have a pet, what is your pet's name? ")
    petName = input("Enter pet name or nothing: ")

    if (petName == ""):
        random_animal_name = ""
        with open("animals.txt") as rFile:
            all_names = rFile.readlines()
            random_animal_name = random.choice(all_names)
        return f"Your band name could be {cityName} {random_animal_name}"
    
    return f"Your band name could be {cityName} {petName}"

print(bandNameGenerator())


    