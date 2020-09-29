from Usage import usage
import sys

def grep(args):
    """print lines that match patterns"""
    vIsTrue = False
    if args[0] == "-v":
        if len(args) < 2:       # check for file name list
            usage("Need search entry", "grep")
            sys.exit(1)
        vIsTrue = True
        args.pop(0)
    searchItem = args.pop(0)    # save the desired search

    if len(args) == 0:
        usage("Too few arguments", "grep")
        sys.exit(1)
    yesList = []
    noList = []
    for file in args:
        f = open(file)
        f.seek(0)
        for line in f.readlines():
            if searchItem in line:
                yesList.append(line)        # if desired search in line then add to yes list
            else:
                noList.append(line)
        f.close()
    if vIsTrue:
        for i in noList:
            print(i, end="")
    else:
        for i in yesList:                   # print the yes list if -v is not present
            print(i, end="")

