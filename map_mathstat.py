#!/usr/bin/env python

import sys
import string
import math


Sum = 0
count = 0
primeNo=0

#reading input from the text file
for line in sys.stdin:
	temp =	line.strip()
	if temp and temp !='':
		number = int(temp)
		#adding the current number to the sum value
		Sum = Sum + number
		#keeping the count of the numbers
		count = count + 1
		numCount = 1
		#calculating the prime numbers
		if number < 2:
			numCount = 0
		elif number == 2:
			numCount = 1
		elif number%2 == 0:
			numCount = 0
		else:
			for i in range(3, int(math.sqrt(number))+1, 2):
				if number % i == 0:
					numCount = 0
					break;	
		if numCount == 1:
			primeNo = primeNo +1


print '%s\t%s' % ('count', count)
print '%s\t%s' % ('sum', Sum)
print '%s\t%s' % ('PrimeNo', primeNo)

