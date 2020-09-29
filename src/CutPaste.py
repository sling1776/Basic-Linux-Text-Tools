from Usage import usage
import sys

def cut(args):
    """remove sections from each line of files"""
    columnsWantedNums = []
 # check for the -f character #
    if args[0] == "-f":
        args.pop(0)
        columnsWanted = args[0].split(",")      # get the string of numbers
        for item in range(len(columnsWanted)):
            if not columnsWanted[item].isdigit():
                usage("A comma-separated field specification is required", "cut")
                sys.exit(1)
            columnsWantedNums.append(int(columnsWanted[item]))  # change the string into numbers
        args.pop(0)
    else:
        columnsWantedNums = [1]     # if no -f then just have the first column as default

# check for filename list #
    if len(args) < 1:
        usage("Too few Arguments", "cut")
        sys.exit(1)
# sort the wanted columns numerically #
    columnsWantedNums.sort()

    for file in args:
        f = open(file)
        for line in f:
            linePrint = line.split(",")         # split the .csv file into its sections by commas
            for column in columnsWantedNums:
                if column > len(linePrint):
                    line = ""
                else:
                    line = linePrint[column-1].replace("\n", "")    # print the column desired, remove any \n characters
                print(line, end="")
                if column == columnsWantedNums[len(columnsWantedNums)-1]: # if the column is the last desired column
                    print()                                               # print the newline character
                else:
                    print(",", end="")                                    # otherwise just print a comma
        f.close()




def paste(args):
    """merge lines of files"""
    fileList = []
# open all the files and put them in a list #
    for file in args:
        f = open(file)
        fileList.append(f)

# find the largest file #
    largestFileIndex = 0
    for index in range(len(fileList)):
        fileList[largestFileIndex].seek(0)
        fileList[index].seek(0)
        lenFile1 = len(fileList[largestFileIndex].readlines())
        lenFile2 = len(fileList[index].readlines())
        if lenFile1 < lenFile2:
            largestFileIndex = index

# reset all read files to beginning #
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
            print(line, end=varEnd)     # print the lines of each file next to each other the last file in line gets \n
# close all the files #
    for file in fileList:
        file.close()
