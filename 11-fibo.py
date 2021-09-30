def u(n):
    u_n_1 = 1
    u_n_2 = 1
    u_n = 1
    while n > 1:
        n = n - 1
        u_n = u_n_1 + u_n_2
        u_n_2 = u_n_1
        u_n_1 = u_n

    return u_n

def u_rec(n):
    if n <= 1:
        return 1
    else:
        return u_rec(n-1) + u_rec(n-2)

for i in range(21):
    print(i, u(i))
print(u_rec(20)) # Attention à ne pas mettre trop ici (< 40)