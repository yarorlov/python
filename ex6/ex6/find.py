#!/usr/bin/env python
import os,sys
import argparse


parser = argparse.ArgumentParser(description = "Find all files with names")
parser.add_argument('path', help='name of files you need to find')
parser.add_argument('-n','--name', action='store', help='name of files you need to find')
parser.add_argument('-p', '--print', action='store_true', help='print searched files')

# Store path 

def path_finder(path):
    if path == '.':
        print(path)
        dir = os.getcwd()            
    else:
        dir = path
    return dir
              
# Store searched files

def search_files(dir, s_name):
    searched_list = []
    whole_dir_list = os.listdir(path=dir)  
    for filename in whole_dir_list:
        if s_name in filename:
            searched_list.append(filename)
    return searched_list

# Print command
def print_file(s_list):
    for el in s_list:
        print(el)    

if __name__ == '__main__':

    args = parser.parse_args()
    searched_dir = path_finder(args.path)
    searched_files_list = search_files(searched_dir, args.name)
    if args.print: print_file(searched_files_list)
    
