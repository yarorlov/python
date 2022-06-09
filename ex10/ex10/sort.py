#!/usr/bin/env python

import os,sys
import argparse

# Parsing sort command. Returns Namespace with path and flags.
def parsing():
    parser = argparse.ArgumentParser(description = "Handling command line arguments.")
    parser.add_argument('-r','--reverse', action='store_true', help='reverse sort')
    parser.add_argument('-f','--fair', action='store_true', help='ignoring case sensitive when sorting')
    parser.add_argument('path', type=str, nargs=1, help='stores path to file or takes any input if "-"')
    args = parser.parse_args()
    return args

# Sort function relies on method "sorted". Takes Namespace from parsing() func as an argument.
def sort(parsed_args):

    if parsed_args.fair:
        case = str.lower
    else: case = None 

    if parsed_args.path[0] == '-':
        lines = sys.stdin.readlines()
    else:
        with open(parsed_args.path[0]) as f:
            lines = f.readlines()

    result = sorted(lines,key=case,reverse=parsed_args.reverse)

    return result


if __name__ == '__main__':

    parsed_args = parsing()
    print(parsed_args)
    for line in sort(parsed_args):
        print(line)