# from enum import Enum

with open("./7/input.txt") as f:
    lines = f.read().strip().split('\n')
# print(lines)

# class FileType(Enum):
#     FILE = 1
#     DIRECTORY = 2

# class File:
#     def __init__(self, name: str, t: FileType, size: int=None):
#        self.name = name
#        self.type = t
#        self.size = size

#     def __str__(self):
#         return f'{self.name}|{self.type}| - {self.size if self.size else ""}'


# class FileTreeNode:
#     def __init__(self, value: File, parent=None):
#         self.value = value
#         self.children = []
#         self.parent = parent

#     def __str__(self):
#         return f'{self.value} <-- parent: {self.parent.value if self.parent else ""}'    

#     def add_child(self, child_node):
#         self.children.append(child_node) 
        
#     # def remove_child(self, child_node):
#     #     self.children = [child for child in self.children 
#     #                         if child is not child_node]

#     def traverse(self):
#         # moves through each node referenced from self downwards
#         nodes_to_visit = [self]
#         while len(nodes_to_visit) > 0:
#             c = nodes_to_visit.pop()
#             print(c)
#             nodes_to_visit += c.children

#     def get_child_by_value(self, value):
#         children = self.children
#         target_node = None
#         for child in children:
#             if child.value.name == value:
#                 target_node = child
#         return target_node
    
#     def get_all_dirs(self):
#         # moves through each node referenced from self downwards
#         nodes_to_visit = [self]
#         dirs = []
#         while len(nodes_to_visit) > 0:
#             c = nodes_to_visit.pop()
#             if c.value.type == FileType.DIRECTORY:
#                 dirs.append(c)
#             nodes_to_visit += c.children
#         return dirs

#     def calculate_size(self) -> int:
#         # recursively calculate size
#         size = 0
#         for child in self.children:
#             if child.value.type == FileType.DIRECTORY:
#                 size += child.calculate_size()
#             else:
#                 size += child.value.size
#         return size


# def how_many_lines_to_next_dollar_or_eof():
#     # pop off the 'ls' line
#     lines.pop()
#     temp = list(reversed(lines))
#     count = 0
#     # print(count,temp[0],len(temp))
#     found = False
#     #
#     while not found:
#         # stop when reach $ or end of file
#         if count >= len(temp) or temp[count][0] == '$':
#             found = True
#             return count
#         count += 1


# # keep track of current directory so that we can add sub dirs as needed
# current_node: FileTreeNode = None
# root: FileTreeNode = None
# # reverse so that we can pop in the correct order
# lines.reverse()

# # create fs tree
# while len(lines) > 0:
#     line = lines.pop().split(' ')
#     # print(line)
#     # check if command
#     if line[0] == '$':
#         if line[1] == 'cd':
#             if not line[2] == '..':
#                 # add a node to the tree
#                 # next line should be an 'ls'
#                 # we need to find out when the next occurence of $ is
#                 # so we can determine when to stop adding files
#                 # root = /

#                 if not root:
#                     root = FileTreeNode(File(name=line[2],t=FileType.DIRECTORY))
#                     current_node = root
#                     print(f'setting the root node {current_node}')
#                 else:
#                     # need to get index of directory since it is already a node in the tree
#                     # print(f'running current_node.get_child_by_value(line[2]) {line[2]}')
#                     current_node = current_node.get_child_by_value(line[2])
#                     # this is not needed because we should have already created the directory
#                     # current_node.add_child(FileTreeNode(File(name=line[2],t=FileType.DIRECTORY), parent=current_node))

#                 # create method for adding n nodes to the tree after the ls
#                 n = how_many_lines_to_next_dollar_or_eof()
#                 for i in range(n):
#                     pos_one,pos_two = lines.pop().split(' ')
#                     # add n nodes as children of the current_node
#                     if pos_one == 'dir':
#                         current_node.add_child(FileTreeNode(value=File(name=pos_two,t=FileType.DIRECTORY), parent=current_node))
#                     else:
#                         current_node.add_child(FileTreeNode(value=File(name=pos_two,t=FileType.FILE, size=int(pos_one)), parent=current_node))
#                 # root.traverse()
#             else:
#                 # move up 1 directory
#                 current_node = current_node.parent

# DISK_SPACE = 70000000
# SPACE_LEFT = DISK_SPACE - root.calculate_size()
# GOAL = 30000000

# lowest_dir_size = 0

# for dir in root.get_all_dirs():
#     size = dir.calculate_size()
#     print(f'dir:{dir} size:{size}')
#     if SPACE_LEFT + size >= GOAL:
#         if size < lowest_dir_size or lowest_dir_size == 0:
#             lowest_dir_size = size

# # root.traverse()
# # print(f'total size = {root.calculate_size()}')
# print(lowest_dir_size)
# print('\n\nfuck this fucking problem!')

# stack based approach
# thanks to primeagen

stack = [['/',0]]
LIMIT = 100000
total = 0
# print(stack[0][0])

for line in lines:
    if line == '$ cd /' or line == '$ ls':
        continue

    if line.startswith('$ cd'):
        dir = line.split(' ')[2]
        if dir == '..':
            name, amount = stack.pop()
            if int(amount) <= LIMIT:
                total += amount
            stack[-1][1] += amount
        else:
            stack.append([dir,0])
        continue


    amount, name = line.split(' ')

    if amount.isnumeric():
        stack[-1][1] += int(amount)
    else:
        # dir
        #stack.push(name, 0)
        pass


print(total)