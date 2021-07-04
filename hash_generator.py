#!/bin/python3
import hashlib,binascii
# making Objects 
#HASHING---------------------------------------------------------------------
md5 = hashlib.md5()#md5 object
sha1 = hashlib.sha1()#sha1 object
sha224 = hashlib.sha224()#sha224 object
sha256 = hashlib.sha256()#sha256 object
sha384 = hashlib.sha384()#sha384 object
sha512 = hashlib.sha512()#sha512 object
blake2s=hashlib.blake2s()#blake2s object
print("\n \n \t\t\t-----> HASHES AVAILABLE <-----\n\n")
print(hashlib.algorithms_available)#printing all available hashes
print('*'*140+"\n"+"\n"+"\n"+"\t\t\t -----> HASHING <-----\n\n")

list_hash_objects = [md5, sha1, sha224, blake2s, sha256, sha384, sha512]#list of all hash objects
S=input("ENTER STRING TO ENCRYPT: \n")#to take input from user

for hash_object in list_hash_objects:
            hash_object.update(S.encode())
            print('-'*140+'\n{}:\t {}\n'.format(hash_object,hash_object.hexdigest()))#printing encrypted data
print('*'*140+"\n"+"\n"+"\n"+"\t\t\t -----> SALTING <-----")           
#----------------------------------------------------------------------------
#SALTING
S1=input("ENTER STRING TO ENCRYPT: \n")
print("\n"+"\n")
hash_list = ['md5', 'sha1', 'sha224', 'sha256', 'sha512']#listing names for hashing
for hash_name in hash_list:
		print("="*150+"\n"+hash_name+":")
		x=hashlib.pbkdf2_hmac(str(hash_name),S1.encode(),b'HASH',10)
		#printing encrypted data with 10 iterations and the salt is HASH
		print(binascii.hexlify(x))
		print(" \nLimiting hashing to 10 characters :\t",end=" ")
		y=hashlib.pbkdf2_hmac(str(hash_name),S1.encode(),b'SALT',5,10)
		#printing encrypted data with 5 iterations and limiting the hash to 10 chahracters and salt is SALT
		print(binascii.hexlify(y))
		
