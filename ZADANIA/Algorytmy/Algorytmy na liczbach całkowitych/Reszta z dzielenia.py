r = int(input())

for i in range(r):
	a, b = map(int, input().split())

	if b < 0:
		print(a % -b)
	else:
		print(a % b)
