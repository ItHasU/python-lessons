compte = 0

def virement(x):
    global compte
    compte += x

print(compte)
virement(500)
print(compte)
