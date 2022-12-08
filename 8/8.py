with open("./8/input2.txt") as f:
    lines = f.read().strip().split('\n')
print(lines)

l = len(lines)
w = len(lines[0])

total_visible = 0

print(f'processing {l} x {w} grid...')
r=0
c=0
for line in lines:
    # skip top and bottom row
    if r == 0 or r == l-1:
        r += 1
        total_visible += len(line)
        continue
    c = 0
    for char in line:
        # skip first and last col
        if c == 0 or c == w-1:
            c += 1
            total_visible += 1
            continue
        # check if tblr are visible to edge
        current = int(char)
        visible_count = 0

        # check left of char
        # using a sublist
        


        # move on to next char
        c += 1
    r += 1

print(total_visible)