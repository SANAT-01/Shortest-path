#!/usr/bin/env python3
 
import sys

minDistance = 9999
currentMinNode = None
neighbors = None
currentNode = None
l = []
final = []

def emit(path):
	return (str(currentNode) + '\t' + str(minDistance) + '\t' + neighbors + '\t' + path)

def map(line):
	#print(line)
	lineValues = line.strip().split("\t",4)
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
	#print(nid + ' NODE ' + str(distance) + ' ' + neighbors + ' ' + str(path))
	l.append(nid + ' NODE ' + str(distance) + ' ' + neighbors + ' ' + str(path))
	
	if neighbors != 'no neighbors':
		adjacencyList = neighbors.split(':')
		for i in range(len(adjacencyList) - 1):
			neighborData = adjacencyList[i].split(',')
			neighbor = neighborData[0]
			currentPath = path + '->' + neighbor
			neighborDistance = distance + int(neighborData[1])
			#print(neighbor + ' VALUE ' +  str(neighborDistance) + ' ' + currentPath)
			l.append(neighbor + ' VALUE ' +  str(neighborDistance) + ' ' + currentPath)


for line in sys.stdin:
	lineValues = line.strip().split(' ')
	nid = int(lineValues[0])
	type = lineValues[1]
	distance = int(lineValues[2])

	if type == 'NODE':
		#print(line,"990909099")
		if currentNode != None:
			if currentMinNode == None:
				currentMinNode = nid
			
			map(emit(path))
			
		path = lineValues[4]
		neighbors = lineValues[3]
		currentNode = nid
		minDistance = distance
		currentMinNode = nid
	else:
		if distance < minDistance:
			minDistance = distance
			currentMinNode = nid
			path = lineValues[3]
map(emit(path))

l.sort()

change = 1

while change :
	change = 0
	minDistance = 9999
	currentMinNode = None
	neighbors = None
	currentNode = None
	final = []
	#print(l)
	l2 = l.copy()
	l2.sort()
	l = []
	for i in l2:
		lineValues = i.strip().split(' ')
		#print(lineValues,len(l))
		nid = int(lineValues[0])
		type = lineValues[1]
		distance = int(lineValues[2])

		if type == 'NODE':
			if currentNode != None:
				if currentMinNode == None:
					currentMinNode = nid

				map(emit(path))
				final.append(emit(path))
			path = lineValues[4]
			neighbors = lineValues[3]
			currentNode = nid
			minDistance = distance
			currentMinNode = nid
		else:
			if distance < minDistance:
				change = 1
				minDistance = distance
				currentMinNode = nid
				path = lineValues[3]
				#final.append(emit(path))
	map(emit(path))
	final.append(emit(path))

l.sort()

for a in final:
	print(a)
