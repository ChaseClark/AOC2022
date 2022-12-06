with open("./5/input.txt") as f:
    lines = f.read().split('\n')

# part 1

# blank_idx = lines.index('')

# num_cols = int(lines[blank_idx-1].strip()[-1])
# num_rows = blank_idx-1

# # convert the stacks of crates into a dict

# stacks = {}
# char_idx = 1

# for c in range(num_cols):
#     stacks[c] = []
#     for r in range(num_rows-1,-1,-1):
#         if len(lines[r]) >= char_idx and not lines[r][char_idx] == ' ':
#             stacks[c].append(lines[r][char_idx])
#     char_idx += 4

# move_list = lines[blank_idx+1:]

# print(stacks)

# def move( amount: int, from_stack: int, to_stack: int):
#     for _ in range(amount):
#         stacks[to_stack-1].append(stacks[from_stack-1].pop())

# for m in move_list:
#     moves = m.split(' ')
#     # 1, 3 ,5
#     move(int(moves[1]),int(moves[3]),int(moves[5]))

# print(stacks)

# message = ''

# for i in stacks:
#     message+=stacks[i].pop()

# print(message)


# part 2
blank_idx = lines.index('')

num_cols = int(lines[blank_idx-1].strip()[-1])
num_rows = blank_idx-1

# convert the stacks of crates into a dict

stacks = {}
char_idx = 1

for c in range(num_cols):
    stacks[c] = []
    for r in range(num_rows-1,-1,-1):
        if len(lines[r]) >= char_idx and not lines[r][char_idx] == ' ':
            stacks[c].append(lines[r][char_idx])
    char_idx += 4

move_list = lines[blank_idx+1:]

print(stacks)

def move( amount: int, from_stack: int, to_stack: int):
    temp_list = []
    for _ in range(amount):
        temp_list.append(stacks[from_stack-1].pop())
    stacks[to_stack-1].extend(reversed(temp_list))

for m in move_list:
    moves = m.split(' ')
    # 1, 3 ,5
    move(int(moves[1]),int(moves[3]),int(moves[5]))

print(stacks)

message = ''

for i in stacks:
    message+=stacks[i].pop()

print(message)