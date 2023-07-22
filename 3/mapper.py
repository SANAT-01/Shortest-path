#!/usr/bin/env python

""" the input file is a file of sorted nodes """
import random as rd
import sys

sources = []
count = 0
n = 100
while count < n:
    i = rd.randint(0,1965206)
    if i not in sources:
        sources.append(i)
        count += 1

sources = list(map(str,sources))
sources.sort()

sources = list(map(int,sources))
l = [[]] # to create a adjancy list of nodes

current_word = None

d = 0 # distances in each iteration

for line in sys.stdin: # iterating trough each lines
    line = line.strip()
    if "#" in line:
        continue
    node, to = line.split('\t', 1) # spliting the lines on the basis of tabs
    if current_word == node:
        l.append(to)
    else:
        if current_word:
            lenght = len(l[0])
            add = n-lenght
            l[0].extend([float("inf")]*add)
            distances_list = l[0]
            
            c = 0
            for y in distances_list:
                y = float(y)
                for x in range(1,len(l)):
                    print("{}\t{}\t{}".format(sources[c],l[x], y + 1))
                print("{}\t{}\t{}".format(sources[c], current_word, l))
                c += 1

            l = [[]]
        if int(node) in sources:
            index = sources.index(int(node))
            l[0].extend([float("inf")]*index)
            l[0].append(0)
        else:
            l[0].append(float("inf"))
        l.append(to)
    
            
        current_word = node

lenght = len(l[0])
add = n-lenght
l[0].extend([float("inf")]*add)
distances_list = l[0]

c = 0
for y in distances_list:
    y = float(y)
    for x in range(1,len(l)):
        print("{}\t{}\t{}".format(sources[c], l[x], y + 1 ))
    print("{}\t{}\t{}".format(sources[c], current_word, l))
    c += 1

