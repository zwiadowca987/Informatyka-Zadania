def suma_bin(z):
    s = 0
    i = z

    while i >= 0:
        s += z % 2
        z = z // 2
        i -= 1

    return s


n = int(input())
print(suma_bin(n))
