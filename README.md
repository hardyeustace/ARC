# The Abstraction and Reasoning Corpus (ARC) - FORKED

This repository has been forked from the fchollet/ARC repo.  This repository contains the ARC task data, as well as a browser-based interface for humans to try their hand at solving the tasks manually.

Three tasks have been choosen and a hand coded solution has been created for each task
0a938d79.json
1a07d186.json
1bfc4729.json
The solutions are in a new directory src and are named 
solution_0a938d79.py
solution_1a07d186.py
solution_1bfc4729.py

To run the files from the command line run
<path to python> <path to one of solution files> <path to one of the three task files>
    e.g.
    >python c:\dev\git\ARC\src\solution_0a938d79.py c:\dev\git\ARC\data\training\0a938d79.json

It should print out the output grid (as a grid of integers, with space as
separator) for each training pair and then each evaluation pair in the task. There should be a blank
line between grids. It should not print anything else
