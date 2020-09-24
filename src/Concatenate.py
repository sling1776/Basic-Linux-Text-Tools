def cat(args):
    """concatenate files and print on the standard output"""
    for file in args:
        f = open(file)
        f.seek(0)
        for line in f.readlines():
            print(line, end="")
        f.close()


def tac(args):
    """concatenate and print files in reverse"""
    for file in args:
        f = open(file)
        f.seek(0)
        backwards = f.readlines()
        backwards.reverse()
        for line in backwards:
            print(line, end="")
        f.close()
