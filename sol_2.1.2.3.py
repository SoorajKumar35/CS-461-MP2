from Crypto.Cipher import AES

ciphertext = ''
with open("2.1.2.3_aes_weak_ciphertext.hex") as f:
	ciphertext = f.read().strip()
ciphertext = ciphertext.decode('hex')


with open("sol_2.1.2.3.hex") as f:
	key = f.read().strip()
key = key.decode('hex')

iv_str = "\x00"*16

cipher = AES.new(key, mode = 2, IV = iv_str)
print cipher.decrypt(ciphertext)


#find correct key and corresponding plaintext
'''with open("2.1.2.3_aes_weak_plaintext.hex",'w') as f:
	for i in range(32):
		key_str = "\x00"*31+chr(i)
		cipher = AES.new(key_str, mode = 2, IV = iv_str)
		plaintext = cipher.decrypt(ciphertext)
		f.write("\n"+str(i)+"\n"+plaintext)'''

#write correct key to solution file
'''with open("sol_2.1.2.3.hex",'w') as f:
	sol = "\x00"*31+chr(25)
	f.write("".join("{:02x}".format(c) for c in sol))'''