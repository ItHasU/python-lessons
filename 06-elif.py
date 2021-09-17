age_str = input("Quel est ton age ? ")
age = int(age_str)

if age < 18:
    print("Tu es trop jeune, aurevoir!")
elif age < 25:
    print("Un peu jeune, mais pas trop, ça va")
else:
    print(f"Bienvenue, ton age est {age}")
