#!/usr/bin/python

import sys
import json

try:
    filename = sys.argv[1]
    data = open(filename, 'r').read()
except IndexError:
    data = sys.stdin.read()

jdata = json.loads(data)
print(json.dumps(jdata, indent=2))
