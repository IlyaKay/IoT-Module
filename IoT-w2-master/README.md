# Worksheet 2

## Overview
The gitlab repository contains:
- <span>README.md</span>
    - The current file, it contains an overview of my worksheet 2 progress and details on how to traverse the repository to find specific things. It also has a comparison of different data structures to their potential application for morse encoding and decoding.
- <span>main.py</span>
    - This file contains a number of function calls that we were told to implement over the course of worksheet 2.
    - The file outlines each task in worksheet and has the corresponding functions called with the notes.
    - This acts as the examples section of the <span>README.md</span> file.
- <span>morse.py</span>
    - This file contains all the classes, methods and functions that are used in the project.
    - Basically all the coding is put in this file. This was done to make it easier to program as the worksheet says that we are not marked on how organised our repository is.
    - It also automatically generates the encode and decode trees at the bottom of the file which makes it easier to run functions if you just want a working tree to produce an output rather than having to create and pass in a new tree every time you call a function.
- <span>morseunit.py</span>
    - This file contains all the assert tests that we were told to make over the progress of the worksheet.
    - These tests have similarities to the examples ran in <span>main.py</span> but do not return any visual outputs for the user to interpret unless they fail.

Accessing files:  
There are no folders in the gitlab repository as there is a small number of files, so to access a file you can simply read about which file you need to access from the list above and select it from the same repository as this file.  
Additional notes if the list above is unclear:
- <span>main.py</span> to access the examples of the code working.
- <span>morse.py</span> to access the main programming (eg. functions).
- <span>morseunit.py</span> to access the assert tests.

Sorry if this sounds condescending due to the repetition, that was not my intention, I am just trying to be safe.

## Binary Trees vs Binary Heaps vs Dictionaries
### A discussion about the differences between encoding and decoding morse messages using binary trees, binary heaps and dictionaries.
  
*First lets outline what each of the data structures are:*  
A binary tree is a type of tree data structure in which each node has at most two children. In the case of a morse tree the order of the tree structure is predetermined by how characters are encoded in morse.  
A binary heap is a type of heap data structure that takes the form of a complete binary tree, meaning that every level of the tree (other than the lowest one potentially) is filled. If the lowest level is not fully filled, whatever values are placed on it are filled from left to right. This allows it to be represented as an array too, simply by reading off of the tree representation from left to right. In the case of a morse heap the order of the tree structure is predetermined by how characters are encoded in morse.  
A dictionary is a data type that is composed of a collection of pairs of values. In the case of morse the dictionary would have a character paired with the morse code equivalent.  
  
*Every data structure has its advantages and disadvantages over the others:*  
Binary trees can execute quickly and the structure of a binary tree is perfect for morse code. This and the fact that adding new characters with a insert function is quite easy makes them very good for use in morse code.  
Binary heaps are similar to binary trees in that they can execute faster than dictionaries but it is very hard to add individual characters onto them for the morse implementation as one of the main benefits of binary heaps is that their nodes are generally ordered between the parents and children but the order has to be specific for morse.  
Dictionaries do not need to be ordered correctly for morse code which means they can even be entered alphabetically as long as the morse messages correspond correctly in their pairs. This makes it very easy to add new characters and matching existing characters when decoding.  
  
In conclusion I think that dictionaries are the best for encoding and decoding messages in morse as they execute effectively  due to being a built in data structure and can add new characters very easily without the need for ordering. The small disadvantage of speed is for the most part negligible.