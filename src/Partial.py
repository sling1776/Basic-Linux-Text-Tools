from Usage import usage
import sys

def head(args):
    """output the first part of files"""
    linesRead = 10

    if args[0] == "-n":
        if len(args) < 2:
            numberNeededError("head")
        if not args[1].isdigit():
            numberNeededError("head")
        linesRead = int(args[1])
        args.pop(0)
        args.pop(0)

    if len(args) == 0:
        needArguments("head")

    for file in args:
        f = open(file)
        if len(args) > 1:
            printHeader(file)
        f.seek(0)
        for line in range(linesRead):
            print(f.readline(), end="")
        print()
        f.close()





def tail(args):
    """output the last part of files"""
    print("TODO: output the last part of files")

def printHeader(filename):
    print(f"==> {filename} <==")

def numberNeededError(tool):
    usage("Number of lines is required", tool)
    sys.exit(1)

def needArguments(tool):
    usage("Too few arguments", tool)
    sys.exit(1)
