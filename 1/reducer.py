#!/usr/bin/env python

import sys

l = []
nodes = {}
current_node = None
total_words = 0
m = ""
data = []

mi = float("inf")

for line in sys.stdin: # iterating trough each lines
    line = line.strip()
    node, dist = line.split('\t', 1) # spliting the lines on the basis of tabs
    try :
        dist = float(dist)
    except :
        pass
    if current_node == node:
        d = dist
    else:
        if current_node:
            m[0] = min(mi,float(m[0])) # to aviod changing the distance of source from 0 to inf
            #print("{}-{}".format(current_node,m))
            nodes[current_node] = m
            mi = float("inf")
            m = ""
            
        current_node = node
        d = dist
    
    if "[" in str(d):
        d = d.replace("inf","\"inf\"")
        m = eval(d)
    elif d < mi:
        mi = d

m[0] = min(mi,float(m[0]))
#print("{}-{}".format(current_node,m))
nodes[current_node] = m
#print(nodes)
change = 1

while change:
    change = 0
    for a in nodes:
        line = nodes[a]
        node = a
        lst = line # spliting the lines on the basis of tabs
        d = float(lst[0])

        for x in range(1,len(lst)):
            data.append(lst[x]+":"+str(d+1))

    data = sorted(data)
    #print(data)
    for z in data:
        node,dist = z.split(":")
        adj_l = nodes[node]
        prev_dist = adj_l[0]
        if prev_dist > float(dist):
            change = 1
            nodes[node][0] = float(dist)
        #print(nodes,dist)
    data = []

for final in (nodes):
    print("{}\t{}".format(final,nodes[final][0]))