x = 3
y = 5

def soustract(a, b):
    return a - b

z = soustract(x, y)
print(f"{x} - {y} = {z}")

z = soustract(a=x, b=y)
print(f"{x} - {y} = {z}")

z = soustract(b=y, a=x)
print(f"{x} - {y} = {z}")

z = soustract(a=y, b=x)
print(f"{y} - {x} = {z}")