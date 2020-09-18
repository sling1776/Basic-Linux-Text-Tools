# Pattern search tool (`grep`)

Find all shades of Blue in our list of colors

    $ python src/tt.py grep Blue data/colors8 
    Royal Blue
    Midnight Blue
    Dodger Blue


The search pattern is case-sensitive; lowercase 'blue' is not present in our
list, hence no results are printed *(notice that the prompt appears immediately following the command)*

    $ python src/tt.py grep blue data/colors8
    $


Searching for capital 'Blue' demonstrates that the pattern may occur anywhere in a line of text:

    $ python src/tt.py grep Blue data/colors8
    Royal Blue
    Midnight Blue
    Dodger Blue


Find all lines containing lowercase letter 'a' across many files:

    $ python src/tt.py grep a data/ages8 data/colors8 data/let3
    Favorite Color
    Royal Blue
    Light Salmon
    DarkSea Green
    Dark Goldenrod
    a


The `-v` argument prints lines that *don't* have a match.  Find all lines *not* containing lowercase `'a'` across many files

    $ python src/tt.py grep -v a data/ages8 data/colors8 data/let3
    Age
    22
    36
    24
    39
    26
    23
    29
    17
    Midnight Blue
    Antique White
    Dodger Blue
    Snow
    b
    c


Styles of locomotion containing the substring 'rch'

    $ python src/tt.py grep rch data/verbs8
    march
    lurch


And the rest...

    $ python src/tt.py grep -v rch data/verbs8
    Locomotion Style
    crawl
    traipse
    push
    trot
    slink
    wriggle


Words containing double 'o's; 200 lines trimmed down to 4!

    $ python src/tt.py grep oo data/words200
    clubroom
    boom
    flooding
    burglarproofed


## Handling errors

The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

Your program must use `usage()` to raise an error when too few arguments are given; at a minimum the name of one input file is required.
