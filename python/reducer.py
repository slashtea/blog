#!/usr/bin/python3.4

import sys


(last_key, max_val) = (None, -9999)

for line in sys.stdin:
    (key, val) = line.strip().split("\t")

    if last_key and last_key != key:
        # if we have a new key.
        print("%s\t%.1f" % (last_key, max_val))
        (last_key, max_val) = (key, int(val) * 0.1)
        # print("from if", last_key)
    else:
        (last_key, max_val) = (key, max(max_val, int(val) * 0.1))
        # print("from else", last_key)

if last_key:
    print("%s\t%.1f" % (last_key, max_val))
