def euklides_rek(x, y):
    if x == y:
        return x
    elif x > y:
        return euklides_rek(x - y, y)
    else:
        return euklides_rek(x, y - x)


def euklides_iter(x, y):
    while x != y:
        if x > y:
            x -= y
        elif x < y:
            y -= x
    return x


def euklides_mod(x, y):
    while y != 0:
        c = x % y
        x = y
        y = c
    return x


a, b = int(input()), int(input())
print(euklides_rek(a, b))
print(euklides_iter(a, b))
print(euklides_mod(a, b))
