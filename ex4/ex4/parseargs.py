import argparse

parser = argparse.ArgumentParser(description = "Handling command line arguments.")

parser.add_argument('-u','--up', action='store_true', 
                    help='print a list with uppercased agruments') # if used, print all arguments in uppercase
parser.add_argument('-n', '--number', action='store_const', const=42, default=1, help=' 42x print option')
parser.add_argument('arguments', metavar='arguments', type=str, nargs='+',
                    help='just arguments')

if __name__ == '__main__':
    args = parser.parse_args()

    if args.up:
        args.arguments = [el.upper() for el in args.arguments]
    
    print(args.arguments * args.number)
    print(args.number)