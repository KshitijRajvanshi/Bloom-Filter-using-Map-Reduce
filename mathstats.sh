#!/bin/bash





hadoop jar /root/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -input /data/numbers -output output -file map_mathstat.py reduce_mathstat.py -mapper map_mathstat.py -reducer reduce_mathstat.py
