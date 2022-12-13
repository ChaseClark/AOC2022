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
    def add_edge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def bfs(self, s):
 
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
 

hills = {}
starting_hill_location = None
g = Graph()


for r in range(len(lines)):
    for c in range(len(lines[0])):
        # add new entry to dict
        # hills[(r,c)] = list(lines[r][c])
        u = (r,c,lines[r][c])
        # check above
        if r - 1 >= 0:
            g.add_edge(u,(r-1,c,lines[r-1][c]))
        # check below
        if r + 1 < len(lines):
            g.add_edge(u,(r+1,c,lines[r+1][c]))
        # check left
        if c - 1 >= 0:
            g.add_edge(u,(r,c-1,lines[r][c-1]))
        # check right
        if c + 1 < len(lines[r]):
            g.add_edge(u,(r,c+1,lines[r][c+1]))

        #check left right up and down from node
        # if hills[(r,c)] == ['S']:
        #     starting_hill_location = (r,c,'S')
        print(g.graph[u])

# bfs

# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
 
# print ("Following is Breadth First Traversal"
#                   " (starting from vertex 2)")
# g.BFS(2)
 