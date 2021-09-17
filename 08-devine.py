import random

age = random.randint(1, 10)
rep = -1
while rep != age:
    rep = int(input("Devine mon age ? "))
    if rep < age:
        print("Un peu plus haut")
    elif age < rep:
        print("Un peu plus bas")

print(f"Bravo, mon age c'était bien {age}")