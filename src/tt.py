#!/usr/bin/env python

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage

import sys


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    tool = sys.argv[1]
    if len(sys.argv) < 3:
        usage("Too few arguments", tool)
        sys.exit(1)

    if tool == "cat":
        cat(sys.argv[2:])
    elif tool == "tac":
        tac(sys.argv[2:])
    elif tool == "head":
        head(sys.argv[2:])
    elif tool == "tail":
        tail(sys.argv[2:])
    elif tool == "wc":
        wc(sys.argv[2:])
    elif tool == "grep":
        grep(sys.argv[2:])
    elif tool == "sort":
        sort(sys.argv[2:])
    elif tool == "paste":
        paste(sys.argv[2:])
    elif tool == "cut":
        cut(sys.argv[2:])

