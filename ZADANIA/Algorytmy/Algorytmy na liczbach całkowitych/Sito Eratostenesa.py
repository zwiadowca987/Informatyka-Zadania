pierwsza = []
R = 2

for i in range(R):
    pierwsza.append(True)

pierwsza[0] = False
pierwsza[1] = False

i = 2
while i * i <= R:
    if pierwsza[i]:
        for j in range(2 * i, R, i):
            pierwsza[j] = False
    i += 1

ile = int(input())

for i in range(ile):
    n = int(input())
    if pierwsza[n]:
        print("TAK")
    else:
        print("NIE")
