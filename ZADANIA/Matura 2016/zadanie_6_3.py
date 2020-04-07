f = open('dane_6_3.txt', 'r')
g = open('wyniki6_3.txt', 'w')

for i in range(3000):
	e, c = map(str, f.readline().split())

	key = ord(c[0]) - ord(e[0])
	if key < 0:
		key += 26

	output = ''

	for char in e:
		if 65 <= ord(char) <= 90:
			s = ord(char) + key
			if s > ord('Z'):
				s -= 26
			output += chr(s)
		elif 97 <= ord(char) <= 122:
			s = ord(char) + key
			if s > ord('z'):
				s -= 26
			output += chr(s)
		else:
			output += char

	if output != c:
		g.write(str(e) + ' ' + str(c) + '\n')

f.close()
g.close()