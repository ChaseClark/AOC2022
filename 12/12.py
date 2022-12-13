from collections import defaultdict

with open("./12/input2.txt") as f:
    lines = f.read().strip().split('\n')

# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")

hills = {}
starting_hill_location = None

for r in range(len(lines)):
    for c in range(len(lines[0])):
        # add new entry to dict
        hills[(r,c)] = list(lines[r][c])
        if hills[(r,c)] == ['S']:
            starting_hill_location = (r,c)

print(starting_hill_location)
# bfs