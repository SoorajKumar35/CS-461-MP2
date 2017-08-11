import sys
import math
import decimal
from Crypto.PublicKey import RSA

def is_odd(x):
	if x%2 == 0:
		return False
	else:
		return True

def is_whole(x,y):
	if x%y == 0:
		return True
	else:
		return False

def convergents(e):
    n = [] # Nominators
    d = [] # Denominators

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else: # i > 1
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)
        yield (ni, di)

def cf_expansion(n, d):
    e = []

    q = n // d
    r = n % d
    e.append(q)

    while r != 0:
        n, d = d, r
        q = n // d
        r = n % d
        e.append(q)

    return e

def find_key(N, e, conv):

	
	for k,d in conv:

		if k == 0:
			continue
		if not is_odd(d):
			continue
		if (e*d-1)%k != 0:
			continue
		phi = (e*d-1)/k
		if solve_prime(N,phi):
			return d;
			

	return 0

def solve_prime(N, phi):
	a = 1
	b = N-phi+1
	c = N
	if (b**2-4*a*c) < 0:
		return False
	if (-b+math.sqrt(decimal.Decimal(b**2-4*a*c)))%(2*a) != 0 or (-b-math.sqrt(decimal.Decimal(b**2-4*a*c)))%(2*a) != 0:
		return False
	return True
	'''x1 = (-b+math.sqrt(decimal.Decimal(b**2-4*a*c)))/(2*a)
	x2 = (-b-math.sqrt(decimal.Decimal(b**2-4*a*c)))/(2*a)
	return [phi,x1,x2]'''


if(len(sys.argv)<5):
	print "No enough arguments."
	exit()

ciphertext_file = sys.argv[1]
key_file = sys.argv[2]
modulo_file = sys.argv[3]
output_file = sys.argv[4]

with open(key_file) as f:
	key_str = f.read().strip()
e = int(key_str,16)


with open(ciphertext_file) as f:
	ciphertext = f.read().strip()

with open(modulo_file) as f:
	modulo = f.read().strip()
N = int(modulo,16)


expansion = cf_expansion(e,N)

conv = convergents(expansion)

prikey = find_key(N,e,conv)



RSAkey = RSA.construct((N,e,prikey))

ciphertext = int(ciphertext,16)

plaintext = RSAkey.decrypt(ciphertext)

print plaintext
#plaintext = hex(plaintext)[2]
with open(output_file,'w') as f:
	f.write(hex(plaintext)[2:])
