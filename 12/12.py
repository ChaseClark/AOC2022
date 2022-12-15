from collections import defaultdict

with open("./12/input2.txt") as f:
    lines = f.read().strip().split('\n')

# This class represents a directed graph
# using adjacency list representation
class graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def add_edge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    # https://onestepcode.com/graph-shortest-path-python/
    # https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
    # https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
    def shortest_path(self, start, target):
        paths = [[start]]
        index = 0
        previous_nodes = {start}    
        # print(paths, previous_nodes)

        if start == target:
            return paths[0]

        while index < len(paths):
            current_path = paths[index]
            last_node = current_path[-1]
            next_nodes = self.graph[last_node]
            # print(f'current_path {current_path},last_node {last_node},next_nodes {next_nodes}')

            # search the goal node
            if target in next_nodes:
                current_path.append(target)
                # print('target found!')
                return current_path
            
            # else we add new paths
            for next_node in next_nodes:
                if not next_node in previous_nodes:
                    new_path = current_path.copy()
                    new_path.append(next_node)
                    paths.append(new_path)
                    # avoid backtracking
                    previous_nodes.add(next_node)
                    # print(f'new_path {new_path},paths {paths}, previous_nodes {previous_nodes}')
            # onward
            index += 1
        return [] # nothing found
        

hills = {}
starting_hill_locations = []
ending_hill_location = None
g = graph()


# dumb func to account for 'E's value
def get_val_from_char(char) -> int:
    if char == 'E': 
        return ord('z') # this needs to be the highest climbable val possible
    if char == 'S':
        return ord('a')
    else:
        return ord(char.lower())

for r in range(len(lines)):
    for c in range(len(lines[0])):
        # add new entry to dict
        # hills[(r,c)] = list(lines[r][c])
        u = f'{r} {c} {lines[r][c]}'
        # check above
        if r - 1 >= 0:
            # check if current letter is less than target
            if get_val_from_char(lines[r][c]) >= get_val_from_char(lines[r-1][c]) - 1:
                g.add_edge(u,f'{r-1} {c} {lines[r-1][c]}')
        # check below
        if r + 1 < len(lines):
            if get_val_from_char(lines[r][c]) >= get_val_from_char(lines[r+1][c]) - 1:
                g.add_edge(u,f'{r+1} {c} {lines[r+1][c]}')
        # check left
        if c - 1 >= 0:
            if get_val_from_char(lines[r][c]) >= get_val_from_char(lines[r][c-1]) - 1:
                g.add_edge(u,f'{r} {c-1} {lines[r][c-1]}')
        # check right
        if c + 1 < len(lines[r]):
            if get_val_from_char(lines[r][c]) >= get_val_from_char(lines[r][c+1]) - 1:
                g.add_edge(u,f'{r} {c+1} {lines[r][c+1]}')

        if lines[r][c] == 'S' or 'a':
            starting_hill_locations.append() f'{r} {c} S'
        if lines[r][c] == 'E':
            ending_hill_location = f'{r} {c} E'
        # print(f'u:{u} {g.graph[u]}')

p = g.shortest_path(starting_hill_location,ending_hill_location)
# print('result: ', p,len(p) - 1)