wyraz = input()
klucz = input()
szyfr = ''

for i in range(len(wyraz)):
	szyfr += chr(ord(wyraz[i]) ^ ord(klucz[i % len(klucz)]))

print(szyfr)