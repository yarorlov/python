import argparse
import os
import sys

# making output file and concatenating .txt files

def output(file_list, file=sys.stdout): # output file option for testing 
    
    output_file = open('output.txt', 'a')
    output_file.truncate(0)
    try:
        for file_name in file_list:
            with open(os.path.abspath(f"{file_name}"), 'r') as f:
                    output_file.write(f.read())
        output_file.close()

        with open("output.txt", 'r') as output:
            print(output.read(), file=file ,end='')
            
    except FileNotFoundError:
        print(f'ERROR. no such {file_name} file')
               
    finally:
         try:
            output_file.close()            
            os.remove("output.txt")
         except:
             print('ERROR. output.txt doesnt exist')

# parsing .txt filenames


parser = argparse.ArgumentParser(description = "cat command")
parser.add_argument('files', metavar='args', type=str, nargs='+',
                        help=' must be .txt files')

if __name__ == '__main__':

    args = parser.parse_args()
    output(args.files)


