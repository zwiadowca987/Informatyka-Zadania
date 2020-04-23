def pot_mod_szybkie(x, y, z):
    if y == 0:
        return 1 % z
    elif y % 2 != 0:
        return (x * pot_mod_szybkie(x, y - 1, z)) % z
    else:
        p = pot_mod_szybkie(x, y // 2, z)
        return (p * p) % z


a, n, d = map(int, input().split())
print(pot_mod_szybkie(a, n, d))
