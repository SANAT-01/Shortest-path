
To find the shortest distance from any source (here we have considerd node 0 as the source node) 
to a given particular node we have implemented a dijkstra algorithm to compute it.
In the mapper we read the input file roadNet-CA.txt, since all the starting nodes are in
order we read them amd print the nodes along with the distances and their adjancy list ,
where the first element as the the min distance of the current node and other as its connected 
nodes in a directed graph. in reducer we compute it using dijkstra algoritm 
where we uses while loop to find the min distnace until there is no change/update in the min distance.

we had also included a test file data2.txt file to check the correctness of the algorithm as the 
roadNet-CA.txt file will take 30-40 min to compute all the distances.

# note : if the the node is not reachable then the distance between them is inf

