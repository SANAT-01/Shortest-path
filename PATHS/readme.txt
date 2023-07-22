
To find the path of nodes from a particular source node we have implemented a dijkstra algorithm to compute it , 
considering the distance between and two nodes i and j will be 1 . in the mapper we read the input file roadNet-CA.txt, 
since all the starting nodes are in order we read them and print the nodes, and a mark (to determine whether it is a node or value)
, its position, the connected nodes(e.g - node1,value:node2,value:) and its path from the source, where the first element as a list containing the the min distance of the current node for the
source in the adjancylist and other as its connected nodes in a directed graph. in reducer we compute it using dijkstra algoritm 
by while loop  until there is no change in the min distance. then using using another for loop we print the output

we had also included a test file data2.txt file to check the correctness of the algorithm as the 
roadNet-CA.txt file will take too long to compute all the distances

# note : if the the node is not reachable then the distance between them is 9999 and path is that node only

