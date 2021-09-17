import random

age = random.randint(1, 10)
rep = -1
while rep != age:
    rep = int(input("Devine mon age ? "))
print(f"Bravo, mon age c'était bien {age}")