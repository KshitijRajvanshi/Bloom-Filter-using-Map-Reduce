#!/usr/bin/env python
import sys
import string
import hashlib
import pickle
file_name = sys.argv[1]
input_data = open(file_name,'r')
data=input_data.read()
records=pickle.loads(data)
input_data.close()
while True:
        word= raw_input('Enter WORD:').lower()
        if word == 'exit':
                break
        hash0 = hashlib.md5(word).hexdigest()
	bits1 = int(hash0,base=16)%1000000
        hash1 = hashlib.md5(word + '1').hexdigest()
        bits2 = int(hash1,base=16)%1000000
	hash2 = hashlib.md5(word + '2').hexdigest()
	bits3= int(hash2,base=16)%1000000
        if records[bits1] == 1 and records[bits2] == 1 and records[bits3] == 1:
            print 'Found'
        else:
            print 'Not Found'

