from Crypto.Cipher import AES
import sys

if(len(sys.argv)<5):
	print "No enough arguments."
	exit()

ciphertext_file = sys.argv[1]
key_file = sys.argv[2]
iv_file = sys.argv[3]
output_file = sys.argv[4]

key_str = ''
iv_str = ''

with open(key_file) as f:
	key_str = f.read().strip()
key_str = key_str.decode('hex')
print key_str

with open(iv_file) as f:
	iv_str = f.read().strip()
iv_str = iv_str.decode('hex')
print iv_str

cipher = AES.new(key_str, mode = 2, IV = iv_str)

ciphertext = ''
with open(ciphertext_file) as f:
	ciphertext = f.read().strip()
ciphertext = ciphertext.decode('hex')

plaintext = cipher.decrypt(ciphertext)


print plaintext
with open(output_file,"w") as f:
	f.write(plaintext)

