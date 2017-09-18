#!/bin/bash




hadoop jar /root/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -input /data/books -output output -file map_bloom.py reduce_bloom.py -mapper map_bloom.py -reducer reduce_bloom.py


