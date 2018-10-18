#!/usr/bin/python3.4

import sys
import re


for lines in sys.stdin:
    lines = lines.strip().split('\n')
    for line in lines:
        year, temperature, q = line[15:19], line[87:92], line[92:93]
        if temperature != "+9999" and re.match("[01459]", q):
            print("%s\t%s" % (year, temperature))
