
To find the local clustering coefficient of nodes we have implemented a dijkstra algorithm to compute it , 
considering the distance between and two nodes i and j will be 1 . in the mapper we read the input file roadNet-CA.txt, 
since all the starting nodes are in order we read them amd print the nodes along with the distances and 
their adjancy list, where the first element as a list containing the the min distance of the current node for different 
sources in the adjancylist and other as its connected nodes in a directed graph. in reducer we compute it using dijkstra algoritm 
by while loop inside for loop which iterates 100 times(for 100 different source)and find the min distance until 
there is no change in the min distance. then using graph.py we plot the scatter plot of it where in  x axis 
the average min diatance and y axis as time taken in milli sec.

we had also included a test file data2.txt file to check the correctness of the algorithm as the 
roadNet-CA.txt file will take too long to compute all the distances
to run the code for test file, in mapper change n and romdom generator by any thing between 0 -24 as the
total no of nodes are 24 and reducer change average to (total distance / 25)

# note : if the the node is not reachable then the distance between them is inf

ans - yes we can see some correllation between them as the computation increases because more 
      connected nodes are present