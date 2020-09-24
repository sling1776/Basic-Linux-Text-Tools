from Usage import usage
import sys

def cut(args):
    """remove sections from each line of files"""
    columnsWantedNums = []
    if args[0] == "-f":
        args.pop(0)
        columnsWanted = args[0].split(",")
        for item in range(len(columnsWanted)):
            if not columnsWanted[item].isdigit():
                usage("A comma-separated field specification is required", "cut")
                sys.exit(1)
            columnsWantedNums.append(int(columnsWanted[item]))
        args.pop(0)
    else:
        columnsWantedNums = [1]

    if len(args) < 1:
        usage("Too few Arguments", "cut")
        sys.exit(1)

    columnsWantedNums.sort()

    for file in args:
        f = open(file)
        for line in f:
            linePrint = line.split(",")
            for column in columnsWantedNums:
                if column > len(linePrint):
                    line = ""
                else:
                    line = linePrint[column-1].replace("\n", "")
                print(line, end="")
                if column == columnsWantedNums[len(columnsWantedNums)-1]:
                    print()
                else:
                    print(",", end="")
        f.close()




def paste(args):
    """merge lines of files"""
    fileList = []
    for file in args:
        f = open(file)
        fileList.append(f)

    largestFileIndex = 0
    for index in range(len(fileList)):
        fileList[largestFileIndex].seek(0)
        fileList[index].seek(0)
        lenFile1 = len(fileList[largestFileIndex].readlines())
        lenFile2 = len(fileList[index].readlines())
        if lenFile1 < lenFile2:
            largestFileIndex = index

    for file in fileList:
        file.seek(0)

    maxFileLen = len(fileList[largestFileIndex].readlines())
    fileList[largestFileIndex].seek(0)
    for i in range(maxFileLen):
        for index in range(len(fileList)):
            if index == len(fileList)-1:
                varEnd = "\n"
            else:
                varEnd = ","
            line = fileList[index].readline().replace("\n", "")
            print(line, end=varEnd)

    for file in fileList:
        file.close()
