#!/usr/bin/env python

"""DIJKSTRA'S ALGORITHM"""
# here we are considering thr node 0 as the source node and we will find the shortest path all other differnrt nodes 

# importing sys module
import sys

l = [] # to create a adjancy list of nodes with first element as its distance from the source node

current_node = None 

d = 0 # distances in each iteration
for line in sys.stdin: # iterating trough each lines
    line = line.strip() # striping the unnecessary characters
    if "#" in line:
        continue
    node, to = line.split('\t', 1) # spliting the lines on the basis of tabs , and extracting the nodes for a particular edge

    if current_node == node:
        l.append(to)
    else:
        if current_node:
            d = l[0]  # extracting the the previous distance value for the "node"
            print("{}\t{}".format(current_node,l)) # emitting the the adjancy list for the node "node"
            # and then emitting its connected nodes with new distance 
            for x in range(1,len(l)): # iterating ove each connected nodes 
                add = ((int(node) + int(l[x])) % 20 ) + 1 # distance increment pattern
                print("{}\t{}".format(l[x], d + add)) # emitting the key and value pairs

            l = [] 
            if node != "0": # ignoring the source node
                l.append(float("inf"))
            l.append(to)
        else :
            if node == "0": # considering 0 as the source node
                l.append(0) # so the first element as the distance
            l.append(to)
            
        current_node = node

print("{}\t{}".format(node,l)) # emitting the last output key and value pair