#!/usr/bin/env python
import sys

args = sys.argv

options=[]

flags = {
    "-v": args,
    "-o": options,
    '-q': 2,
    '--help': "HELP MESSAGE",
    '-h': "HELP MESSAGE"

}



for el in args:
    if not el.startswith("-"):
        options.append(el)
        

for el in flags:
    if el in args:
        print(flags[el])