f = open('dane_6_2.txt', 'r')
g = open('wyniki6_2.txt', 'w')

L = []
X = []
n = 3001
for i in range(n):
	try:
		string = f.readline()
		wyraz, klucz = map(str, string.split())
		L.append(str(wyraz))
		if klucz.strip() == '':
			X.append(0)
		else:
			X.append(int(klucz.strip()))
	except StopIteration:
		break
output = ''
ile = 0

for j in L:
	O_ILE_PRZESUNAC = X[ile] % 26
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
	ile += 1

f.close()
g.close()