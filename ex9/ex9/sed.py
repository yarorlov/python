#!/usr/bin/env python
import os,sys
import argparse
import re

# Parsing flags, replacements and path
parser = argparse.ArgumentParser(description = "Handling command line arguments.")
parser.add_argument('-i','--inplace', action='store_true', help='changing strings in-place')
parser.add_argument('-f','--fields', action='store')
parser.add_argument('-b','--bytes', action='store')
parser.add_argument('-c','--characters', action='store')
parser.add_argument('rep', type=str, nargs=1)
parser.add_argument('path', type=str, nargs=1)

def sed(pat, repl, path, **flags):

    # In-place replacement in file (-i flag)
    if flags['inplace']:
        with open(path, 'r+', encoding = 'utf-8') as f:
            data = f.readlines()
            print(data)
            f.seek(0)
            for lin in data:
                lin = re.sub(pat, repl, lin)
                print(lin)
                f.write(lin)
           

    # Basic implementation of REGEXP
    with open(path, 'r+', encoding = 'utf-8') as f:
            data = f.readlines()
            print(data)
            result = ''
            for lin in data:
                lin = re.sub(pat, repl, lin)
                result += ''.join(lin)
                
            return result

if __name__ == '__main__':
    args = parser.parse_args()
    rep = args.rep[0].split('/')
    
    # How to implement all flags with kwargs?

    flags = {'inplace':False}
    if args.inplace: flags['inplace'] = True
    print(flags)

    print(sed(rep[1], rep[2], args.path[0], **flags))