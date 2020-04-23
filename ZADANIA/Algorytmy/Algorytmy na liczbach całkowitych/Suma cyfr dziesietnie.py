def suma_dz(x):
    s = 0
    i = x

    while i >= 0:
        s += x % 10
        x = x // 10
        i -= 1

    return s


n = int(input())
print(suma_dz(n))
