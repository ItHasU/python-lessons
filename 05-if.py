age_str = input("Quel est ton age ? ")
age = int(age_str)

if age < 18:
    print("Tu es trop jeune, aurevoir!")
    exit()
else:
    print(f"Bienvenu, ton age est {age}")
