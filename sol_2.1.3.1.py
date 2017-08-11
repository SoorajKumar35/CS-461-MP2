import sys
import string
from Crypto.Cipher import AES
import base64
from Crypto.Hash import SHA256

#get strings
f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")
f3 = open(sys.argv[3], "w")

input_string = f1.read()
perturbed_string = f2.read()

#calculate hashes of both strings
hash_fn1 = SHA256.new(input_string)
hash_fn2 = SHA256.new(perturbed_string)

hash1_bin = hash_fn1.digest()
hash1_hex = hash_fn1.hexdigest()

hash2_bin = hash_fn2.digest()
hash2_hex = hash_fn2.hexdigest()

# # #print hash1_bin
# #print hash1_hex
# # #print hash2_bin
# #print hash2_hex

# byte_string = "\x01\x03"
# byte_string_bin = base64.b16decode(hash1_hex, casefold = True)
# #print int(hash2_hex,16)
# byte_string_bin = hash1_hex.decode('hex')
# string_int = byte_string_bin
# #print int(byte_string_bin,10)
# #print int(hash1_bin,10)

#Calculate xored solution of the two hex values outputted from the hash function previously
hash1_int = int(hash1_hex,16)
hash2_int = int(hash2_hex,16)
#print hash1_int
#print hash2_int

xor = hash1_int ^ hash2_int

num_of_setbits = bin(xor).count("1")

#print xor
#print num_of_setbits

output = hex(num_of_setbits)[2:]

f3.write(output)







