f = open('dane_6_1.txt', 'r')
g = open('wyniki6_1.txt', 'w')

L = []
n = 100
for i in range(n):
	liczba = f.readline()
	L.append(liczba)
output = ''
O_ILE_PRZESUNAC = 107 % 26

for j in L:
	for char in j:
		if 65 <= ord(char) <= 90:
			s = ord(char) + O_ILE_PRZESUNAC
			if s > ord('Z'):
				s -= 26
			output += chr(s)
		elif 97 <= ord(char) <= 122:
			s = ord(char) + O_ILE_PRZESUNAC
			if s > ord('z'):
				s -= 26
			output += chr(s)
		else:
			output += char

	g.write(output)

f.close()
g.close()