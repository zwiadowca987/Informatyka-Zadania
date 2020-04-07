n = input().strip()
output = ''

P = []

for i in range(4):
    P.append(['#'] * 100)

zwrot = -1
w = 0
for i in range(len(n)):
    P[w][i] = n[i]
    if w == 0 or w == 3:
        zwrot = -zwrot
    w += zwrot

for i in range(4):
    for j in range(len(n)):
        if P[i][j] != '#':
            output += P[i][j]

print(output)