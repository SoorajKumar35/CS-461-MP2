from fractions import gcd
from Crypto.PublicKey import RSA
'''
class remainTree(object):
	def __init__(self, data,levels):
		self.data = data
		self.root = data[level]


	def build_tree(self, leafNum):'''

def build_level(data):
	if not isinstance(data, list):
		print "argument is not a list!!!"
		return -1
	level = []
	for x1,x2 in zip(data[0::2],data[1::2]):
		level.append(x1*x2)
	return level
		
def build_pTree(level):
	if not isinstance(level, list):
		print "argument is not a list!!!"
		return -1
	
	levels = 0
	tree = []
	data = level;
	tree.append(data)
	levels += 1
	while(len(data) > 1):
		data = build_level(data)
		tree.append(data)
		levels += 1

	return levels, tree

def remainTree(ptree, levels):
	if not isinstance(ptree, list):
		print "argument is not a list!!!"
		return -1

	n = levels
	#rtree = []
	n -= 1
	ret = ptree[n]
	
	#rtree.append(pre)
	while n > 0:
		level = []
		n -= 1
		data = ptree[n]
		k = 0
		for x in ret:
			y1 = data[k]
			y2 = data[k+1]		
			level.append(x%(y1**2))
			level.append(x%(y2**2))
			k += 2
		#rtree.append(level)
		ret = level
	return ret
	'''	

	n = 0
	for item in ret:
		item = gcd(item//ptree[0][n], ptree[0][n])
		n += 1

	return ret'''

def calcGCD(A,B):
	if (len(A) != len(B)):
		return 0
 	for i in range(len(A)):
 		A[i] = gcd(A[i]//B[i],B[i])
 	return A


def calcD(phi, e):
 	d = []
 	for x in phi:
 		k = 1;
 		while (k*x+1)%e != 0:
 			k+=1
 		d .append((k*x+1)/e)
 	return d


M =[]
with open("moduli.hex") as f:
	M = f.readlines()
M = [int(x.strip(),16) for x in M]
print len(M)

#M = [2,4,6,8]
levels, ptree = build_pTree(M)
#print ptree
#print levels
#print ptree[0][0]

remain = remainTree(ptree,levels)

print remain
print len(remain)

Gcd = calcGCD(remain, M)
e = 65537
phi = []
for i in range(len(M)):
	if Gcd[i] > 1 and Gcd[i] < M[i]:
		p = Gcd[i]
		q = M[i]//p
		phi.append((q-1)*(p-1))

d = calcD(phi,e)

print d
with open("2.2.5_ciphertext.enc.asc") as f:
	ciphertext = f.read().strip()

with open("rsa_output") as f:


	for key in d:
		RSAkey = RSA.construct((N,e,prikey))

		ciphertext = int(ciphertext,16)

		plaintext = RSAkey.decrypt(ciphertext)

		print plaintext
	#plaintext = hex(plaintext)[2]
		f.write(hex(plaintext)[2:])

print Gcd

