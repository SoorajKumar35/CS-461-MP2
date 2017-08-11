import sys
import string
from Crypto.Cipher import AES
from pymd5 import md5, padding

f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")
f3 = open(sys.argv[3], "w")

query = f1.read()
command = f2.read()
m = '&user=admin&command1=ListFiles&command2=NoOp'
number_of_bits =(len(m) + 8 + len(padding((len(m)+8)*8)))*8
# print number_of_bits
h = md5(state = query[6:38], count = number_of_bits)
# print len('867e9cdc121d98c791d31e647a3c643a')
# print query[6:38]

h.update(command)
# print h.hexdigest()

f3.write( query[0:6] + h.hexdigest() + query[38:len(query)] + command)




