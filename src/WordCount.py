def wc(files):
    """print newline, word, and byte counts for each file"""
    tChar = 0
    tWord = 0
    tLine = 0
    for file in files:
        f = open(file)
        f.seek(0)
        character = " "
        characterCount = -1          # for the extra EOF character at the end of each file
        wordCount = 0
        lineCount = 0
        while character != "":
            character = f.read(1)
            characterCount += 1
            if character == " " or character == "\n" or character == "\t":
                wordCount += 1
            if character == "\n":
                lineCount += 1
        print(lineCount, "\t", wordCount, "\t", characterCount, "\t", file)
        tChar += characterCount
        tWord += wordCount
        tLine += lineCount
    if len(files) > 1:
        print(tLine, "\t", tWord, "\t", tChar, "\t", "total")
