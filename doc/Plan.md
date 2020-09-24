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

**Design a process for obtaining the output from the input.  Consider both *good*
and *bad* inputs.  Find or create examples of both kinds of input.

Work out problem examples on paper, on a whiteboard or some other medium that
is *not* your computer.  It is a mistake to begin writing executable code
before you thoroughly understand what form the algorithm(s) must take.

Instead, describe components of the system in *"pseudocode"*.  Expect to make
lots of mistakes at this point.  You will find that it is much easier to throw
away pseudocode than real code.  

Manually work through several examples that illustrate the program's overall
purpose, as well as the purpose of each component of the finished system.  You
will converge on a correct solution much faster if you feel comfortable making
mistakes as you go.

This phase involves the use of many levels of abstraction to decompose the
problem into manageable components, and design strategies for implementing each
component.  Components may be functions, modules or classes.**

cat(args)
 


# 3.  Function Template

**Combine the function stubs written in step #1 with pseudocode from step #2.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.

One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.

If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.

When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #3 as tests and ensure that each
function passes all.  Doing so discovers mistakes.  Tests also supplement
examples in that they help others read and understand the definition when the
need arises—and it will arise for any serious program.

As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.

If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.

At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.  

The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
