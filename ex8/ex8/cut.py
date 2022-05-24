#!/usr/bin/env python
import os,sys
import argparse

parser = argparse.ArgumentParser(description = "Handling command line arguments.")

parser.add_argument('-d','--delimiter', action='store', 
                    help='print a list with uppercased agruments')
parser.add_argument('-f','--fields', action='store')
parser.add_argument('-b','--bytes', action='store')
parser.add_argument('-c','--characters', action='store')
parser.add_argument('path', type=str, nargs=1)

# cut

# -d delimiter

# -f fields

# -b bytes

args = parser.parse_args()

print(args.path)

if args.delimiter:
    print(args.delimiter)

with open(args.path[0], 'r', encoding ='utf-8') as f:
    sample = f.readlines()
    print(sample)

# line = input() - implementation of a standard input. If you want list of fields separated with comma like '5,6,7'
# then just for fields_at = [i for i in args.fields.split(',')]. If you want fields like '5-7', then split args.fields
# for 2 numbers start_field = 5, end-_field=7 and the fields_at = [i for i in range(start_field, end_field+1)]

if args.delimiter and args.fields:
    for el in sample:
        s_line = el.split(args.delimiter)
        print(s_line)
        print(s_line[int(args.fields)-1])    

if args.bytes :
    for el in sample:
        b_line = el.encode()[:(int(args.bytes))]
        b_line = b_line.decode(encoding ='utf-8')
        print(b_line)

if args.characters:
    for el in sample:
        print(el[:int(args.characters)])