def sort(args):
    """sort lines of text files"""
    myList = []
    for file in args:
        f = open(file)
        for line in f.readlines():
            myList.append(line)
        f.close()
    myList.sort()
    for line in myList:
        print(line, end="")
