#!/usr/bin/env python

import sys
import string
import math

count = 0
Sum = 0
primeNo=0
for line in sys.stdin:
	(key,val) = line.strip().split('\t')
	if key == 'sum':	
		Sum = Sum + int(val)
	elif key == 'PrimeNo':
		primeNo = primeNo + int(val)
	else:
		count = count + int(val)		
print 'Count of Numbers is:' + str(count)
print 'Sum of numbers is:' + str(Sum)
print 'Prime Number Count is:' + str(primeNo)

