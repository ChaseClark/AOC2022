with open("./5/input2.txt") as f:
    lines = f.read().split('\n')

# separate boxes into a list of lists

blank_idx = lines.index('')

num_cols = int(lines[blank_idx-1].strip()[-1])
num_rows = blank_idx-1

# convert the stacks of crates into a dict

stacks = {}
char_idx = 1

for i in range(num_rows-1, -1, -1):
    stacks[i] = []
    print(f'i - {i}')
    for j in range(num_cols):
        print(f'j - {j}')
        if len(lines[i]) >= char_idx:
            stacks[i].append(lines[i][char_idx])
            char_idx += 4
        else:
            stacks[i].append(' ')
    char_idx = 1 

def move( amount: int, from_col: int, to_col: int):
    pass


print(stacks)