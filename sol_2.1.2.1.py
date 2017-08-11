import sys

if(len(sys.argv)<4):
	print "No enough arguments."
	exit()

cipher_text = sys.argv[1]
key_file = sys.argv[2]
output = sys.argv[3]

key_str = list(open(key_file,'r').read().strip())
#print key_str
cipher_str = list(open(cipher_text,'r').read())
#print cipher_str
plain_str = []

for char in cipher_str:
	if char >= 'A' and char <= 'Z':
		idx = key_str.index(char)
		plain_str.append(''.join(chr(ord('A')+idx)))
	else:
		plain_str.append(char)

with open(output,"w") as f:
	for char in plain_str:
		f.write(char)
