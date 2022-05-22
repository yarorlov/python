#!/usr/bin/env python
import re
import sys
import glob




def pattern_matching(pattern, filename):
    matched = []
    with open(f'{filename}', 'r', encoding='utf-8') as s:
        sample = s.readlines()
        for line in sample:
            check = re.search(pattern, line)
            if check:
                matched.append(line)
    return matched

def grep(pattern, data):
    script, pattern, data = sys.argv
    list_of_files = glob.glob(data)
    for el in list_of_files:
        print(f'-----------------checking {el}---------------')
        result = pattern_matching(pattern, el)
        if result:
            for line in result:
                print(f'{el}: ',line )

if __name__ == '__main__':
    grep(pattern, data)
