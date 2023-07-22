#!/usr/bin/env python

"""the input file is a file of sorted nodes"""

import sys

l = [] # to create a adjancy list of nodes

current_word = None

d= 0 # distances in each iteration
for line in sys.stdin: # iterating trough each lines
    line = line.strip()
    if "#" in line:
         continue
    node, to = line.split('\t', 1) # spliting the lines on the basis of tabs
    if current_word == node:
        l.append(to)
    else:
        if current_word:
            d = l[0]
            print("{}\t{}".format(current_word,l))
            for x in range(1,len(l)):
                print("{}\t{}".format(l[x], d + 1))

            l = []
            if node != "0":
                l.append(float("inf"))
            l.append(to)
        else :
            if node == "0":
                l.append(0)
            l.append(to)
            
        current_word = node

print("{}\t{}".format(node,l))