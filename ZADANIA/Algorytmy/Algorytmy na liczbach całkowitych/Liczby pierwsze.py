import math


def is_prime(number):
    if number < 2:
        return False

    sqrt = int(math.sqrt(number))

    for i in range(2, sqrt + 1):
        if number % i == 0:
            return False
    return True


n = int(input())

if is_prime(n):
    print("TAK")
else:
    print("NIE")
