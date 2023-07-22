#!/usr/bin/env python

""" the input file is a file of sorted nodes """
import random as rd
import sys

current_word = None
l = ""
d = 0 # distances in each iteration

def map(line):
	lineValues = line.strip().split()
	nid = lineValues[0]
	#print(lineValues)
	distance = int(lineValues[1])
	neighbors = 'no-neighbors'
	if len(lineValues) > 2:
		neighbors = lineValues[2]
	path = nid

	if len(lineValues) > 3:
		path = lineValues[3]
		elements = path.split('->')
		if elements[len(elements) - 1] != nid:
			path = lineValues[3] + '->' + nid
	print(nid + ' NODE ' + str(distance) + ' ' + neighbors + ' ' + str(path));
	
	if neighbors != 'no neighbors':
		adjacencyList = neighbors.split(':')
		for i in range(len(adjacencyList) - 1):
			neighborData = adjacencyList[i].split(',')
			neighbor = neighborData[0]
			currentPath = path + '->' + neighbor
			neighborDistance = distance + int(neighborData[1])
			print(neighbor + ' VALUE ' +  str(neighborDistance) + ' ' + currentPath)



for line in sys.stdin: # iterating trough each lines
    line = line.strip()
    if "#" in line:
        continue
    node, to = line.split('\t', 1) # spliting the lines on the basis of tabs
    
    if current_word == node:
        l = l + to  + ",1:"
    else:
        if current_word is not None:
            if current_word == "0":
                #print("{} {} {}".format(current_word, 0, l))
                emits = "{} {} {}".format(current_word, 0, l)
            else:
                #print("{} {} {}".format(current_word, 9999, l))
                emits = "{} {} {}".format(current_word, 9999, l)
            map(emits)
        current_word = node
        l = to  + ",1:"
if current_word == "0":
    #print("{} {} {}".format(current_word, 0, l))
    emits = "{} {} {}".format(current_word, 0, l)
else:
    #print("{} {} {}".format(current_word, 9999, l))
    emits = "{} {} {}".format(current_word, 9999, l)
map(emits)