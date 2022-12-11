# with open("./9/input2.txt") as f:
#     lines = f.read().strip().split('\n')
# # print(lines)
# print('starting day 9...')
# # start over
# # part 1

# dirs = {}
# dirs['R'] = [1,0]
# dirs['L'] = [-1,0]
# dirs['U'] = [0,1]
# dirs['D'] = [0,-1]

# class position:
#     def __init__(self,x:int = 0, y:int = 0) -> None:
#         self.x = x
#         self.y = y
#         self.symbol = '.'

#     def __str__(self) -> str:
#         return f'({self.x},{self.y})'

# # class for rope that will keep track of pos of head and tail
# class rope:
#     def __init__(self) -> None:
#         # create a head and a link to the previous node
#         self.head = segment(symbol='H',next_segment=segment('T'))
#         print(f'S:{self.head.position}', end=' ')

#     def move_head(self,dir: str, amount: int):
#         x,y = dirs[dir]
#         # move head
#         for i in range(amount):
#             self.head.prev_position = position(self.head.position.x,self.head.position.y)
#             # print(self.head.prev_position)
#             self.head.position.x += x 
#             self.head.position.y += y
#             print(f'|{dir}{i+1}| - H:{self.head.position}', end=' ')
#             self.head.next_segment.update(self.head)


# class segment:
#     prev_position : position
#     visited = []
#     def __init__(self, next_segment, symbol = '.', ) -> None:
#         self.position = position(0,0)
#         self.symbol = symbol
#         self.next_segment = next_segment

#     def __str__(self) -> str:
#         return f'({self.position.x},{self.position.y})'

#     def update(self, head) -> None:
#         # tail move logic
#         # if tail is overlapping or within 1 pos then dont move
#         x_dif = head.position.x - self.position.x
#         y_dif = head.position.y - self.position.y
#         print(f'x|{x_dif}| y|{y_dif}|',end=' ')
#         if abs(x_dif) <= 1 and abs(y_dif) <= 1:
#             pass # do nothing
#         else:
#             self.position = head.prev_position
#         # check if we have another segment to update
#         print(f'T:{self.position} --{head.prev_position}')
#         # check if tail has visited this spot
        
#         if not (str(self.position) in self.visited):
#             self.visited.append(str(self.position))
#             # print(f'tail visited new location \t\t---> {self.position}')

    
# r = rope()
# # r.move_head('R',4)
# # r.move_head('U',4)

# for line in lines:
#     d,a = line.split(' ')
#     r.move_head(d,int(a))

# # for seg in r.head.next_segment.visited:
# #     print(seg)
# print(len(r.head.next_segment.visited))
# print('fin')

# part 2
with open("./9/input2.txt") as f:
    lines = f.read().strip().split('\n')
# print(lines)
print('starting day 9...')
# start over
# part 1

dirs = {}
dirs['R'] = [1,0]
dirs['L'] = [-1,0]
dirs['U'] = [0,1]
dirs['D'] = [0,-1]

class position:
    def __init__(self,x:int = 0, y:int = 0) -> None:
        self.x = x
        self.y = y
        self.symbol = '.'

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

# class for rope that will keep track of pos of head and tail
class rope:
    def __init__(self) -> None:
        # create a head and a link to the previous node
        self.head = segment(symbol='H',
        next_segment=segment(symbol='1', 
        next_segment=segment(symbol='2',
        next_segment=segment(symbol='3',
        next_segment=segment(symbol='4',
        next_segment=segment(symbol='5',
        next_segment=segment(symbol='6',
        next_segment=segment(symbol='7',
        next_segment=segment(symbol='8',
        next_segment=segment(symbol='9'
        )))))))))) # lmaooooo
        # self.head = segment(symbol='H',
        # next_segment=segment(symbol='1'))
        # print(f'S:{self.head.position}', end=' ')

    def move_head(self,dir: str, amount: int):
        x,y = dirs[dir]
        # move head
        for i in range(amount):
            # self.head.prev_position = position(self.head.position.x,self.head.position.y)
            prev_pos = position(self.head.position.x,self.head.position.y)
            # print(self.head.prev_position)
            self.head.position.x += x 
            self.head.position.y += y
            # print(f'|{dir}{i+1}| - H:{self.head.position}', end=' ')
            self.head.next_segment.update(self.head, prev_pos)


class segment:
    prev_position : position
    visited = []
    def __init__(self, next_segment = None, symbol = '.') -> None:
        self.position = position(0,0)
        self.symbol = symbol
        self.next_segment = next_segment

    def __str__(self) -> str:
        return f'({self.position.x},{self.position.y})'

    def update(self, prev_segment,prev_segment_prev_position) -> None:
        # tail move logic
        # if tail is overlapping or within 1 pos then dont move
        x_dif = prev_segment.position.x - self.position.x
        y_dif = prev_segment.position.y - self.position.y
        prev_pos = position(self.position.x,self.position.y)
        # print(f'x|{x_dif}| y|{y_dif}|',end=' ')
        if abs(x_dif) <= 1 and abs(y_dif) <= 1:
            pass # do nothing
        else:
            self.position = prev_segment_prev_position
        # check if we have another segment to update
        # check if tail has visited this spot
        
        if self.next_segment:
            # print('this node has another segment behind it!')
            self.next_segment.update(self,prev_pos)

        if self.symbol == '9':
            if not (str(self.position) in self.visited):
                self.visited.append(str(self.position))
    
r = rope()
# r.move_head('R',4)
# r.move_head('U',4)

for line in lines:
    d,a = line.split(' ')
    r.move_head(d,int(a))

# for seg in r.head.next_segment.visited:
#     print(seg)
print(len(r.head.next_segment.visited))
print('fin')