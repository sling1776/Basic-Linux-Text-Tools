*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions


I need to create a program that will run similar to a command line prompt in linux.
A lot of the same things that are used in the linux terminal will be created in 
my program. These are the cat/tac, cut/paste, grep, head/tail, sort, and wc commands.

The cat/tac argument will print a concatenation of two files given after the argument.
"tac" is the reversal of cat.

cut/paste will print the columns of the file. Cut will take a CSV file and print the column 
desired. If more than one column is entered then it will print them side by side separated by a comma.
Paste will take text files and print them side by side separated by a comma. 

grep will find all the lines that have a certain phrase or word in them. -v included in the argument will 
print all that don't have that phrase in them.

head/tail will print the first "x" lines or last "x" lines of a file respectively. default is 10 lines. tail does not
reverse the order of the lines. They remain in the same order they were in in the file.

sort will sort the contents of the file alphabetically. This means that numbers are treated 
as strings through this function. 

wc will count the number of words in the file. It prints the lines, words and characters
used in the file.




# 1.  System Analysis

input will come from the command line. No interactive prompts. It will then read files
given from the command line. 

output will be printed to the screen. 

No Formulas

cat
input:list of strings (["data/let3", "data/num2"])
output: print a string: file contents by line with second file following it.
concatenate files and print on the standard output

tac
input:list of strings (["data/let3", "data/num2"])
output: print a string: file contents of first by line backwards with second file backwards following it.
concatenate and print files in reverse

cut
input: list of strings: ["-f", "2", "data/people.csv"]
output:the desired column (2) printed on screen
remove and print sections from each line of files

paste:
input:list of strings (["data/let3", "data/num2"])
output:similar to cat, but the files share the same line
merge lines of files

grep
input: list of strings: ["-v", "a", "data/ages8", "data/colors8", "data/let3"]
output: print all the lines of the files that have/don't have the phrase in them.
print lines that match patterns

head
input: list of strings: ["-n", "3", "data/ages8", "data/names8", "data/words200"]
output: header of file(if more than one) and number of lines from beginning (3)
print first part of file

tail
input: list of strings: ["-n", "3", "data/ages8", "data/names8", "data/words200"]
output: header of file(if more than one) and number of lines (3) towards the end
print last part of file

sort
input: list of strings: ["data/words5", "data/names8"]
output: an alphabetical list of all lines of both files
sort lines of text files

usage
input: error message or tool error
output: error message 
Provide a unified error reporting interface

wc
input: list of Strings: ["data/let3", "data/random20", "data/words200", "data/dup5"]
output: one line per file of lines, words, then characters followed by name of file.
print newline, word, and byte counts for each file


# 2.  Functional Examples

cat(args)
    Check for a file name -> if no then call usage
    loop through all files
        open file 
        go to beginning
        loop through lines in file
            print line
        close file

tac(<filename list>)
    check for a file name -> if no then call usage(tool=tac, error: to few arguments)
    loop through all files
        open file
        go to beginning of file
        loop through all lines of the file using readlines().reverse()
            print line
        close file

head(<-n>, <int>, <filename list>)
    if first arg = "-n"
        check length of args > 3: if not call usage(error too few arguments)
        check if args[1] is num: if not call usage(error provide number)
            convert number from string
            default =10 or number
            remove -n and number from the list of arguments
        loop through file name list
            open file
            go to the beginning
            loop for lines to read
                print line that is read
             close file
 
wc(<filename list>)
    loop for all files
        open file
        go to beginning of file
        loop for all characters in file
            charactercoount +=1
            if character == " " of "\n" then 
                wordcount +=1
            if character == "\n"
                line count +=1
        print (line, word, character, filename)
        add totals to total
        close file
    print out total 

tail(<-n>, <int>, <filename list>)
    check for -n -> use same a  head
    loop through files
        get number of lines from file
        loop for number desired
            add last line to newlist
        reverse new list
        loop 
            print all lines of new list
        close files
        
grep(<-v><string><filelist>)
    check for -v then remove from arguments
    save "string" and remove from arguments
    check for len() of arguments -> if no files ->error not enough arguments
    loop for all files
        for line in f.readlines()
            if "string" in line 
                add to yes list
            else add to no list
        if check -v
            print no list
        else print yes list

sort(<filelist>)
    loop for all files
        open file
        save contents into list
    sort list alphabetically
    print list
    
paste(<filelist>):
    filelist=[]
    fir all files in file list args
        open file
        append file to file list
    find largest file
    for lines in largest file
        for all files
            print line in file end="," unless it is the last in file list, then end="\n"
    for all files 
        close files

cut(<-f> <numberstring> <file list>)
    columns wanted = list with a 0 in it
    check for -f
        pop from arguments
        split numberstring(",") = columns wanted
    for item in columns wanted
        if item isdigit
            change item to int
        else error
        pop numberstring from args
    for all files in file list
        for all lines in file
            split line by commas
            for all desired columns
                print desired column end=","
        close file

# 3.  Function Template

done


# 4.  Implementation

completed.

# 5.  Testing

All tests should be done on the commandline.
tests for each tool:
    <toolname> no other arguments passed
        output: usage error(too few arguments)
    <toolname> improper file name given
        output: program crash with python error

cat tool
    <cat> single file
        output: print contents to screen
    <cat> multiple files
        output: print contents of each file to screen in order that they were given
    
tac tool
    <tac> single file
        output: print contents to screen in reverse
    <tac> multiple files
        output: print contents of each file in reverse to screen in order that they were given
        
head tool
    <head> no number given
        output: print first 10 lines of given file
    <head> number given
        output: print first *number* of lines from file
    <head> mulitple files given with number as well
        output: file header with first *number* of lines from file. all files printed.
    <head> multiple files with one DNE file
        output: print lines from each file until DNE file then give python error message and crash
    
tail tool
    same tests as head. the output should give the last *number* of lines from the file
    
wc tool
    <wc> multiple files
        output: print lines, words, characters, filename to screen. totals at bottom.
    <wc> multiple files with a DNE file
        output: print lines words, characters, filename until DNE file and then crash and give python error

grep tool
    <grep> without string
        output: error too few arguments
    <grep>  <-v> 
        output: print all lines without the string
    <grep> with string multiple files
        output: print all lines with the string of all files in order
        
sort tool
    <sort> file list
        sort alphabetically

paste tool
    <paste> multiple files
        output: give each line of the file next to each other separated by commas
                when a file runs out of lines to give then just print a blank.
    
cut tool
    <cut> .csv files
        print first lines of each file
    <cut> .csv files with <-f>
        print the columns wanted with the -f. these will be sorted in order.
    
    
After running these tests I could find no issues with my code.
