import sys
import math
import decimal
from Crypto.PublicKey import RSA

if(len(sys.argv)<5):
	print "No enough arguments."
	exit()

ciphertext_file = sys.argv[1]
key_file = sys.argv[2]
modulo_file = sys.argv[3]
output_file = sys.argv[4]

with open(key_file) as f:
	key_str = f.read().strip()
d = int(key_str,16)
with open(ciphertext_file) as f:
	ciphertext = f.read().strip()
ciphertext = int(ciphertext,16)
with open(modulo_file) as f:
	modulo = f.read().strip()
N = int(modulo,16)
print d
print N
e = int("3",16)
RSAkey = RSA.construct((long(N),long(e),long(d)))
plaintext = RSAkey.decrypt(ciphertext)
with open(output_file,'w') as f:
	f.write(hex(plaintext)[2:])
