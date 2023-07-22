#!/usr/bin/env python

import sys
from datetime import datetime

def route(d, mi, m):
    try :
        d = float(d)
    except :
        pass

    if "[" in str(d):
        d = d.replace("inf","\"inf\"")
        m = eval(d)
    elif d < mi:
        mi = d
    return mi,m
    

l = []
list_source = [] # contains all nodes with their adjacency list with differert nodes as source node
nodes = {} 
current_node = None
current_node2 = None
m = "" # it is the adjancy list for a particular node
data = []
mi = float("inf") # setting min as inf
count_source = 0

for line in sys.stdin: # iterating trough each lines
    line = line.strip()
    src, node, dist = line.split('\t', 2) # spliting the lines on the basis of tabs

    if current_node == src:
        try :
            dist = float(dist)
        except :
            pass

        if current_node2 == node:
            d = dist
        else:
            if current_node2:
                m[0][count_source] = min(mi,float(m[0][count_source])) # to aviod changing the distance of source from 0 to inf
                nodes[current_node2] = m # dictioanry creation for all nodes
                mi = float("inf")
                m = ""

            current_node2 = node
            d = dist
        
        mi,m = route(d,mi,m)

    else:
        if current_node:
            m[0][count_source] = min(mi,float(m[0][count_source])) # to aviod changing the distance of source from 0 to inf
            nodes[current_node2] = m # dictioanry creation for all nodes
            mi = float("inf")
            m = ""
            list_source.append(nodes)
            nodes = {}
            count_source += 1

        current_node = src
        current_node2 = node
        
        mi,m = route(dist,mi,m)

m[0][count_source] = min(mi,float(m[0][count_source])) # to aviod changing the distance of source from 0 to inf
nodes[current_node2] = m
list_source.append(nodes)

source_count = 0

for nodes in list_source:
    change = 1
    now = str(datetime.now())
    now = float(now[14:16]) + float(now[17:])/60
    while change:
        avg_dist = 0
        change = 0
        for a in nodes:
            lst = nodes[a]
            
            node = a # spliting the lines on the basis of tabs
            d = float(lst[0][source_count])

            for x in range(1,len(lst)):
                data.append(lst[x]+":"+str(d+1))
            
        data = sorted(data)
        
        for z in data:
            node,dist = z.split(":")
            adj_l = nodes[node]
            prev_dist = adj_l[0][source_count]
            if (float(prev_dist), float(dist)) == (float("inf"),float("inf")):
                continue
            avg_dist += min(float(prev_dist), float(dist))
            if float(prev_dist) > float(dist):
                change = 1
                nodes[node][0][source_count] = float(dist) # we can also stop this
            
        data = []
        
    end = str(datetime.now())
    end = float(end[14:16]) + float(end[17:])/60
    print("{}\t{}".format(avg_dist/1965206, (end-now)*60000))
    
    source_count += 1