#!/usr/bin/env python

import pickle
import sys
import string

bloom = [0]*1000000
for line in sys.stdin:
	(key,val) = line.strip().split('\t')
	bloom[int(val)] = 1
bloom_filter=pickle.dumps(bloom)
print bloom_filter

