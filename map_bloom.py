#!/usr/bin/env python
import sys
import hashlib
import string
import math
for line in sys.stdin:
	words =	line.strip()
	if words and words !='':
                #removing punctuation
                #converting to lower case
		temp = words.strip().lower().translate(None,string.punctuation).split()
		for word in temp:
                        
#first hash
			hash0 = hashlib.md5(word).hexdigest()
			bits1 = int(hash0,base=16)%1000000
			
#second hash
        		hash1 = hashlib.md5(word + '1').hexdigest()
        		bits2 = int(hash1,base=16)%1000000
        		
#third hash
		        hash2 = hashlib.md5(word + '2').hexdigest()
		        bits3 = int(hash2,base=16)%1000000
			print '%s\t%s' % ('1', bits1)
			print '%s\t%s' % ('1', bits2)
			print '%s\t%s' % ('1', bits3)	

