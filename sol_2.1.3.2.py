import sys
import string
from Crypto.Cipher import AES

f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "w")

input_binarystr = ' '.join(format(ord(x), 'b') for x in f1.read())
input_binarystr_list = input_binarystr.split()
mask = 1073741823
outhash = 0

#print input_binarystr
print input_binarystr_list
#print int('100000',2)

for byte in input_binarystr_list:
	input_byte = int(byte,2)
	# #print 'input_byte',input_byte
	inter_value = ((input_byte^204)<<24) | ((input_byte^51)<<16) | ((input_byte^170)<<8) | (input_byte^85)
	#print 'xored', format(input_byte^204, '02x')
	#print 'left shift', format((input_byte^204)<<24, '02x')
	temp = (outhash & mask) + (inter_value & mask)
	#print 'outhash and mask',(outhash & mask)
	# #print 'intervalue', bin(inter_value)[2:]
	# #print 'mask', bin(mask)[2:]
	#print 'inter_value and mask',(inter_value & mask)
	# #print bin(inter_value & mask)
	#print 'temp',temp

	outhash = temp
	# #print '%x',inter_value
	#print 'outhash',outhash
print hex(outhash)[2:]

f2.write(hex(outhash)[2:])



